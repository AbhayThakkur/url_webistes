# I created this file-Abhay

from django.http import HttpResponse

def sites_1(request):
    return HttpResponse('''<h1>site_1</h1><a href="https://leetcode.com/">LeetCode</a>
    <h1>site_2</h1><a href="https://github.com/">GitHub</a>
    <h1>site_3</h1><a href="https://ocw.mit.edu/">MIT OpenCourseWare</a>
    <h1>site_4</h1><a href="https://www.coursera.org/">Coursera</a>
    <h1>site_5</h1><a href="https://www.researchgate.net/">ResearchGate</a>''')
