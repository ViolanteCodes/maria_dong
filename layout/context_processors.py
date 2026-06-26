def nav_menu(request):
    return {
        "nav_menu": [
            {
                "url_name": "books_list", "label": "Books"
            },
            {
                "url_name": "events", "label": "Press"
            },
            {
                "url_name": "about", "label": "About"
            },
            {
                "url_name": "publications", "label": "Words"
            },
            {
                "url_name": "newsletter", "label": "Newsletter"
            },
            {
                "url_name": "link_tree", "label": "Links"
            },
        ]
    }
