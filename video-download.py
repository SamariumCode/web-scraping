import requests
import re
from bs4 import BeautifulSoup

qualities = {
    '144': 0,
    '240': 1,
    '360': 2,
    '480': 3,
    '720': 4,
    '1080': 5
}

class VideoDownloadException(Exception):
    pass

class QualityError(VideoDownloadException):
    pass

class Scraper:
    def __init__(self, url, quality):
        self.url = url
        self.quality = str(quality)  # Ensure quality is a string
    
    def get_all_links(self):
        result = requests.get(self.url)
        content = BeautifulSoup(result.text, 'html.parser')
        video_links = content.find_all('a', href=re.compile('.mp4'))

        links = [link["href"] for link in video_links]
        links.reverse()  # Reverse the order of links to match with qualities order
        return links
    
    def get_link(self):
        links = self.get_all_links()
        available_links = self.get_qualities()

        if self.quality not in available_links:
            raise QualityError(f'This quality is not available. \n Available qualities are {available_links}')
        
        else:
            link = links[qualities[self.quality]]
            return link

    def get_qualities(self):
        links = self.get_all_links()
        qua = list(qualities.keys())

        available_qualities = []
        for i in range(len(links)):
            available_qualities.append(qua[i])

        return available_qualities

class Main:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(self.url, self.quality)

    def download(self):
        video_url = self.scraper.get_link()
        with open('video.mp4', 'wb') as f:
            print('Downloading video...')
            result = requests.get(video_url, stream=True)
            total_size = result.headers.get('content-length')
            if total_size is None:
                f.write(result.content)
            else:
                download = 0
                total_size = int(total_size)
                for data in result.iter_content(chunk_size=2048):
                    f.write(data)
                    download += len(data)
                    done = int(50 * download / total_size)
                    print('\r[%s%s] %d%%' % ('=' * done, ' ' * (50 - done), done * 2), end='')

        print('\nDownload completed.')

# Example usage
a = Main(url='https://www.namasha.com/v/HxvgmayC', quality='144')
a.download()
