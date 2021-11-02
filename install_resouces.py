import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

package_list = ['numpy', 'pandas', 'matplotlib', 'folium', 'plotly', 'opendatasets', 'dash']

for i in package_list:
    install(i)