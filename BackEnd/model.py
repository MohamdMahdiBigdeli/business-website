class About():
    def __init__(self, title, heading, since, Text, btnText, btnLink, thumb):
        self.title = title
        self.heading = heading
        self.since = since
        self.Text = Text
        self.btnText = btnText
        self.btnLink = btnLink
        self.thumb = thumb


class Blog():
    def __init__(self, title, excerpt, thumb, content, publishDate, author):
        self.title = title
        self.excerpt = excerpt
        self.thumb = thumb
        self.content = content
        self.publishDate = publishDate
        self.author = author


class BlogAuthor():
    def __init__(self, name, designation, proPic, socials):
        self.name = name
        self.designation = designation
        self.proPic = proPic
        self.socials = socials


class BlogAuthorSocials():
    def __init__(self, facebook, twitter, linkedin):
        self.facebook = facebook
        self.twitter = twitter
        self.linkedin = linkedin


class BrandLogo():
    def __init__(self, id, logoSrc, URL):
        self.id = id
        self.logoSrc = logoSrc
        self.URL = URL


class CallToAction():
    def __init__(self, title, text, btnText, btnLink):
        self.title = title
        self.text = text
        self.btnText = btnText
        self.btnLink = btnLink


class Features():
    def __init__(self, id, title, text, imgSrc):
        self.id = id
        self.title = title
        self.text = text
        self.imgSrc = imgSrc


class Funfact():
    def __init__(self, id, counterNumber, counteText):
        self.id = id
        self.counterNumber = counterNumber
        self.counteText = counteText


class HowWeWorks():
    def __init__(self, id, title, text, icon):
        self.id = id
        self.title = title
        self.text = text
        self.icon = icon


class Services():
    def __init__(self, id, title, shortDesc, thumb, previewImages, aboutServiceDesc, features):
        self.id = id
        self.title = title
        self.shortDesc = shortDesc
        self.thumb = thumb
        self.previewImages = previewImages
        self.aboutServiceDesc = aboutServiceDesc
        self.features = features


class Sidebar():
    def __init__(self, id, cate_name, cate_link):
        self.id = id
        self.cate_name = cate_name
        self.cate_link = cate_link


class Slider():
    def __init__(self, id, title, text, bg, btnText, btnLink):
        self.id = id
        self.title = title
        self.text = text
        self.bg = bg
        self.btnText = btnText
        self.btnLink = btnLink


class PricingTable():
    def __init__(self, id, planName, currencyType, planPrice, subscribePlan, planFeatures):
        self.id = id
        self.planName = planName
        self.currencyType = currencyType
        self.planPrice = planPrice
        self.subscribePlan = subscribePlan
        self.planFeatures = planFeatures


class SocialNetworks():
    def __init__(self, id, networkName, username):
        self.id = id
        self.networkName = networkName
        self.username = username


class Team():
    def __init__(self, id, name, designation, profilePic):
        self.id = id
        self.name = name
        self.designation = designation
        self.profilePic = profilePic


class Testimonial():
    def __init__(self, id, quote, author, authorThumb, designation):
        self.id = id
        self.quote = quote
        self.author = author
        self.authorThumb = authorThumb
        self.designation = designation
