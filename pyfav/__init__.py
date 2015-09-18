try:
  from pyfav import get_favicon_url
  from pyfav import parse_markup_for_favicon
  from pyfav import download_favicon
except:
  from pyfav.pyfav import get_favicon_url
  from pyfav.pyfav import parse_markup_for_favicon
  from pyfav.pyfav import download_favicon
