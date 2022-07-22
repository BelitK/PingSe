from ping import Ping
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

sites = ['www.google.com','belitk.tech','abc.abc.com','www.google.com','www.google.com','www.google.com','www.google.com','www.google.com','www.google.com','belitk.tech','www.diken.com.tr','abc.abc.com','www.google.com','www.google.com','www.google.com','www.google.com','www.google.com','www.google.com']
result= pd.DataFrame(columns=['Site','Ping avg return (ms)','Ping errors return'])
for site in sites:
    r = Ping(site)
    
    # print(site)
    # print(f'Ping avg return: {r.avg} ms')
    # print(f'Ping errors return: {r.returncode} {r.stderr}')
    if r.returncode==0:
        data={
        "Site":site,
        'Ping avg return (ms)': r.avg,
        'Ping errors return': "200"
        }
    else:
        data={
        "Site":site,
        'Ping avg return (ms)': "-",
        'Ping errors return': "Error"
        }
    result=result.append(data,ignore_index=True)

fig, ax = plt.subplots()

# hide axes\
with PdfPages(r'C:\Users\blkmrkt\Desktop\mar-228\test.pdf') as export_pdf:
    fig.patch.set_visible(False)
    ax.axis('off')
    #ax.axis('tight')
    ax.table(cellText=result.values, colLabels=result.columns, loc='best')
    plt.title("Request Results")
    fig.tight_layout()

    export_pdf.savefig()
print(result)
