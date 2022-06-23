from app.settings import CAPTCHA_DEMO_URL
from app.solution import Solution

if __name__ == '__main__':
    # num = 1
    # for i in range(2):
    Solution(CAPTCHA_DEMO_URL).resolve()
