import numpy as np
from taipy.gui import Gui, Markdown
import pages

# TO ACTIVATE ENVIRONMENT: C:/Users/jcof2/anaconda3/Scripts/activate
#                           conda activate base 


page_dict = {
    '/': pages.root_page,
    'home':pages.home_page
}


if(__name__=='__main__'):
    Gui(pages = page_dict, 
        css_file='./STYLES/style.css').run( title="SouthPool",
                                            use_reloader=True,
                                            stylekit=False)


