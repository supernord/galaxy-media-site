"""Content for data section - tools, workflows and help tabs."""

galaxy_au_support_item = {
    "title_html": 'Galaxy Australia support',
    "description_html": """<p>
            Any user of Galaxy Australia can request support through an
            online form.
        </p>""",
    "button_link": "/request/support",
    "button_html": "Request support",
}

tools = [
    # {   # Accordion item schema:
    #     "title_html": '',
    #     "description_html": """""",
    #     "inputs": [
    #         {
    #             'datatypes': [''],
    #             'label': '',
    #         },
    #     ],
    #     "button_link": "",
    #     "button_html": "",
    #     "button_tip": "",
    #     "view_link": "",
    #     "view_html": "",
    #     "view_tip": "",
    # },
    {
        "title_html": '<code>MaxQuant</code>',
        "description_html": '<p>MaxQuant is a quantitative proteomics software package designed for analyzing large mass-spectrometric data sets.</p>',
        "inputs": [
            {'datatypes': ['thermo.raw']},
            {'datatypes': ['mzML']},
            {'datatypes': ['mzXML']},
            {
                'datatypes': ['tabular'],
                'label': 'Experimental design template',
            },
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=toolshed.g2.bx.psu.edu/repos/galaxyp/maxquant/maxquant/",
    },
    {
        "title_html": '<code>TMT Analyst</code>',
        "description_html": '<p>Analyze and Visualize Label-Free Proteomics output from MaxQuant.</p>',
        "inputs": [
            {
                'datatypes': ['txt'],
                'label': 'Protein groups (MaxQuant output)',
            },
            {
                'datatypes': ['txt'],
                'label': 'Experimental Design Matrix (MaxQuant output)',
            }
        ],
        "button_link": "https://usegalaxy.org.au/root?tool_id=interactive_tool_tmtanalyst",
        "view_link": "Shah AD, Goode RJA, Huang C, Powell DR, Schittenhelm RB. LFQ-Analyst: An easy-to-use interactive web-platform to analyze and visualize proteomics data preprocessed with MaxQuant. https://doi.org/10.1021/acs.jproteome.9b00496",
    }
]


help = [
    {
        "title_html": 'TMT-Analyst: Manual',
        "description_html": """
            <p>
              A detailed user manual for TMT-Analyst.
            </p>""",
        "button_link": "https://analyst-suites.org/apps/tmt-analyst/TMT-Analyst-manual.pdf",
        "button_html": "Manual",
    },
    {
        "title_html": 'MaxQuant and MSstats for the analysis of TMT data',
        "description_html": """
        <p>
          Learn how to use MaxQuant and MSstats for the analysis of TMT labelled shotgun (DDA) data.
        </p>""",
        "button_link": "https://training.galaxyproject.org/training-material/topics/proteomics/tutorials/maxquant-msstats-tmt/tutorial.html",
        "button_html": "Tutorial",
    },
    galaxy_au_support_item,
]
