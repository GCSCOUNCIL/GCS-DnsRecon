import setuptools

print('''

░██████╗░░██████╗░█████╗░░█████╗░░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗██╗░░░░░
██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗██║██║░░░░░
██║░░██╗░╚█████╗░██║░░╚═╝██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║██║░░╚═╝██║██║░░░░░
██║░░╚██╗░╚═══██╗██║░░██╗██║░░██╗██║░░██║██║░░░██║██║╚████║██║░░██╗██║██║░░░░░
╚██████╔╝██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║╚█████╔╝██║███████╗
░╚═════╝░╚═════╝░░╚════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝╚══════╝
-----------------------------------------------------------------------------
Developer: Harshal(Error404)
Developed by: GCSCOUNCIL
Company: GCSCOUNCIL
''')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GCS-DnsRecon",
    version="1.0.0",
    author="GCS Council",
    author_email="support@gcscouncil.com",
    description="DNS Enumeration Script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darkoperator/dnsrecon",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    scripts=['bin/dnsrecon'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('/etc/dnsrecon', [
            'namelist.txt',
            'snoop.txt',
            'subdomains-top1mil-20000.txt',
            'subdomains-top1mil-5000.txt',
            'subdomains-top1mil.txt',
        ]
        )
    ],
)
