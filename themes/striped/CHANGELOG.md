# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## 2018-04-02
### Added
- Adding styling for side-by-side images in `figure` blocks:
```
<div class="side-by-side-wrapper">
  <figure>
    <img src="images/A.JPG">
    <figcaption>Optional caption</figcaption>
  </figure>
  <img src="images/B.JPG">
</div>
```

## 2018-02-17
### Added
- support for isso comments by defining `ISSO_BASE_URL`
- allow to NOT be indexed by search engines by setting `NOINDEX = True`

## 2018-02-07
### Added
- Adding `CSS_DARK_BACKGROUND` / `CSS_LIGHT_BACKGROUND` configuration properties to optionally customize the grey background style
