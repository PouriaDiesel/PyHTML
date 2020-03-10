""""
    @author : PouriaDiesel
    @email  : pouria.diesel@gmail.com
    @GitHub : github.com/PouriaDiesel
    PouriaDiesel All Rights @2019 Reserved.
"""

from django.conf import settings
from django.template import Template, Context
import django

import lxml.html
import os

import wx
import wx.html2

# Current project directory
Root = os.path.dirname(os.path.abspath(__file__))


# Create a browser by using wxPython library.
class PyBrowser(wx.Dialog, wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        wx.Frame.__init__(self, None, title="Default Frame", style=wx.DEFAULT_FRAME_STYLE)
        self.Maximize(True)
        self.SetLayoutDirection(wx.Layout_LeftToRight)
        self.browser = wx.html2.WebView.New(self)


# For using python projects before using wxPython
def django_init():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        }
    ]
    settings.configure(TEMPLATES=TEMPLATES, TIME_ZONE='UTC', USE_TZ=False)
    django.setup()


# return address of templates directory for local using HTML address.
def temp_addr(view, prefix):
    if prefix:
        return 'file://' + Root + "/" + "templates/" + view
    return "templates/" + view


# create a browser windows and render the htmlView and view it in browser
def render_a_html(htmlView, htmlOut, context):
    f = open(temp_addr(htmlView, False), 'r')
    text = f.read()
    f.close()

    t = Template(text)
    c = Context(context)

    f = open(temp_addr(htmlOut, False), 'w')
    f.write(t.render(c))
    f.close()

    source = lxml.html.parse(temp_addr(htmlOut, False))
    title = source.find(".//title").text

    app = wx.App()
    dialog = PyBrowser(None, -1)
    dialog.SetTitle(title)
    dialog.browser.LoadURL(temp_addr(htmlOut, True))
    dialog.Show()
    app.MainLoop()
