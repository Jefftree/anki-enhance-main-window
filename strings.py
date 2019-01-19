# Associate to each column its title
header = {
    "learning card":_("Learning")+"<br/>"+_("(card)"), 
    "learning later":_("Learning")+"<br/>"+_("later")+" ("+_("review")+")" ,
    "learning now":_("Learning")+"<br/>"+_("now") ,
    "learning all":_("Learning")+"<br/>"+_("now")+"<br/>("+_("later today")+"<br/>("+_("other day")+"))",
    "review due":_("Due")+"<br/>"+_("all") ,
    "review today":_("Due")+"<br/>"+_("today") ,
    "review":_("Due")+"<br/>"+_("today")+" ("+_("all")+")",
    "unseen":_("Unseen")+"<br/>"+_("all")  ,
    "new":_("New")+"<br/>"+_("today") ,
    "unseen new":_("New")+"<br/>"+"("+_("Unseen")+")",
    "buried":_("Buried"),
    "buried/suspended":_("Buried")+"/<br/>"+_("Suspended"),
    "suspended":_("Suspended"),
    "cards":_("Total"),
    "notes/cards":_("Total")+"/<br/>"+_("Card/Note"),
    "notes":_("Total")+"<br/>"+_("Note"),
    "today":_("Today"),
    "undue":_("Undue"),
    "mature":_("Mature"),
    "mature/young":_("Mature"+"/<br/>"+_("Young"),),
    "young": _("Young"),
    "marked":_("Marked"),
}
def getConfAux(conf,field,dic):
    """If field is in headerConf, returns its value.
    otherwise, return the value associated to this configuration's name in dic

    conf -- a configuration from json
    field -- a field name
    dic -- a dictionnary containing the default values if the field is absent
    """
    headerConf = conf.get(field)
    if headerConf is not None:
        return headerConf
    else:
        return dic[conf["name"]]

def getHeader(conf):
    """The header for the configuration in argument"""
    return getConfAux(conf,"header",header)

# Associate to each column its overlay
overlay = {
    "learning card":_("Cards in learning")+"<br/>"+_("""(either new cards you see again,""")+"<br/>"+_("or cards which you have forgotten recently.")+"<br/>"+_("""Assuming those cards didn't graduate)"""),
    "learning later":_("Review which will happen later.")+"<br/>"+_("Either because a review happened recently,")+"<br/>"+_("or because the card have many review left."),
    "learning now":_("Cards in learning which are due now.")+"<br/>"+_("If there are no such cards,")+"<br/>"+_("the time in minutes")+"<br/>"+_("or seconds until another learning card is due"),
    "learning all":_("Cards in learning which are due now")+"<br/>"+_("(and in parenthesis, the number of reviews")+"<br/>"+_("which are due later)"),
    "review due":_("Review cards which are due today")+"<br/>"+_("(not counting the one in learning)"),
    "review today":_("Review cards you will see today"),
    "review":_("Review cards cards you will see today")+"<br/>"+_("(and the ones you will not see today)"),
    "unseen":_("Cards that have never been answered"),
    "new":_("Unseen")+ _("cards")+ _("you will see today")+"<br/>"+_("(what anki calls ")+_("new cards"),
    "unseen new":_("Unseen cards you will see today")+"<br/>"+_("(and those you will not see today)"),
    "buried":_("number of buried cards,")+"<br/>"+_("(cards you decided not to see today)"),
    "buried/suspended":_("number of buried cards,")+"<br/>"+_("(cards you decided not to see today)")+_("number of suspended cards,")+"<br/>"+_("(cards you will never see")+"<br/>"+_("unless you unsuspend them in the browser)"),
    "suspended":_("number of suspended cards,")+"<br/>"+_("(cards you will never see")+"<br/>"+_("unless you unsuspend them in the browser)"),
    "cards":_("Number of cards in the deck"),
    "notes/cards":_("Number of cards/note in the deck"),
    "notes":_("Number of cards/note in the deck"),
    "today":_("Number of review you will see today")+"<br/>"+_("(new, review and learning)"),
    "undue":_("Number of cards reviewed, not yet due"),
    "mature/young":_("Number of cards reviewed, with interval at least 3 weeks/less than 3 weeks"),
    "mature":_("Number of cards reviewed, with interval at least 3 weeks"),
    "young": _("Number of cards reviewed, with interval less than 3 weeks"), 
    "marked":_("Number of marked note")
}
def getOverlay(conf):
    """The overlay for the configuration in argument"""
    return getConfAux(conf,"overlay",overlay)

