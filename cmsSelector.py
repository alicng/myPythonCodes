def cms_selector(lst, txt):


    return [ i for i in lst if txt in i]
            

a=cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru")
print(a)

#