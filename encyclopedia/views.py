from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request):
    return render(request, "encyclopedia/dereck.html", {
        "title": util.get_entry()
    })
