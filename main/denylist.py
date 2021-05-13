# not allowed to create account with these as username
DISALLOWED_USERNAMES = [
    "about",
    "abuse",
    "account",
    "accounts",
    "admin",
    "administration",
    "administrator",
    "api",
    "auth",
    "authentication",
    "billing",
    "blog",
    "blogs",
    "cdn",
    "collection",
    "config",
    "contact",
    "dash",
    "dashboard",
    "developer",
    "developers",
    "docs",
    "documentation",
    "help",
    "helpcenter",
    "home",
    "image",
    "images",
    "img",
    "index",
    "knowledgebase",
    "legal",
    "login",
    "logout",
    "man",
    "manual",
    "meta",
    "metrics",
    "on",
    "ops",
    "pricing",
    "privacy",
    "profile",
    "random",
    "register",
    "registration",
    "search",
    "settings",
    "setup",
    "signin",
    "signup",
    "smtp",
    "static",
    "status",
    "support",
    "terms",
    "test",
    "tests",
    "tmp",
    "wiki",
    "www",
]

# not allowed to create a blog page with these as slugs
DISALLOWED_PAGE_SLUGS = [
    "blog",
    "dashboard",
    "rss",
    "newsletter",
    "notifications",
    "billing",
    "webring",
    "import",
    "export",
    "images",
    "analytics",
    "pages",
]

# elements allowed to exist inside the HTML of a markdown text
ALLOWED_HTML_ELEMENTS = [
    "a",
    "abbr",
    "acronym",
    "article",
    "b",
    "bdi",
    "bdo",
    "br",
    "blockquote",
    "cite",
    "code",
    "div",
    "dfn",
    "em",
    "kbd",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "iframe",
    "img",
    "li",
    "mark",
    "ol",
    "p",
    "pre",
    "q",
    "rb",
    "rt",
    "rtc",
    "ruby",
    "s",
    "samp",
    "section",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "time",
    "u",
    "ul",
    "var",
    "wbr",
]

# attributes allowed to exist inside the elements of the HTML of a markdown text
ALLOWED_HTML_ATTRS = [
    "alt",
    "class",
    "height",
    "href",
    "id",
    "seamless",
    "src",
    "style",
    "title",
    "width",
    "frameborder",
]

# css rules allowed to exist as inline styles on HTML elements of a markdown text
ALLOWED_CSS_STYLES = [
    "background",
    "border",
    "border-radius",
    "color",
    "display",
    "height",
    "width",
]
