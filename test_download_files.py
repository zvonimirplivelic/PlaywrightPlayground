def test_download_vs_code(page):
    page.goto("https://code.visualstudio.com/")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download for Windows").click()
    download = download_info.value
    download.save_as('./download_files/vs_code.txt')
        
def test_download_python(page):
    page.goto("https://www.python.org/downloads/")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Python").click()
    download = download_info.value
    download.save_as('./download_files/python.txt')

def test_download_postman(page):
    page.goto("https://www.postman.com/downloads/")
    with page.expect_download() as download_info:
        page.locator("[data-test=\"download-the-app-windows-64\"]").click()
    download = download_info.value
    download.save_as('./download_files/postman_download.txt')

def test_download_git(page):
    page.goto("https://git-scm.com/downloads")
    page.get_by_role("link", name="Windows", exact=True).click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="64-bit Git for Windows Setup").click()
    download = download_info.value
    download.save_as('./download_files/git.txt')