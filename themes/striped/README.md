This is a fork of [Andrey Novikov](https://github.com/andreynovikov/pelican-html5up-striped) template, based on the [HTML5UP Striped theme](http://html5up.net/striped), to be used as [Pelican](http://getpelican.com/) theme.

Theme features and enhancements:

1. Contains tag cloud (via `tag_cloud` Pelican plugin). Can be disabled by setting `DISPLAY_TAGS_ON_SIDEBAR=False`.
2. Support for avatar specified by `PROFILE_IMG_URL` configuration setting.
3. Support for Disqus & Isso comments, `DISQUS_SITENAME` / `ISSO_BASE_URL` should be set in configuration.
4. Support for Google Analytics, `GOOGLE_ANALYTICS` should be set in configuration.
5. Support for Google site verification by HTML tag, `GOOGLE_SITE_VERIFICATION` should be set in configuration.
6. Articles can contain header image which is shown on index pages and ignored in article. Image is specified with `image` file metadata.
7. Pages can redirect to other locations. Useful if you want to add some external link to main rubricator. Location is specified with `redirect` file metadata.
8. In order for the website to NOT be indexed by search engines, you can set `NOINDEX = True`


## License

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />Le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution Unported</a>
