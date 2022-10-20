{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP2s0sn/cP21+us22V/jg7H",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/abdikeem/Data_Science/blob/Docs/Python_Quiz.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Create a DataFrame from a dictionary of lists"
      ],
      "metadata": {
        "id": "uNiot8qLRy1g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd"
      ],
      "metadata": {
        "id": "cue2EC2QR0xb"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### init a dataframe by dict with different index"
      ],
      "metadata": {
        "id": "MlaJbcf0SSgZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "d = {\"a\": {\"a1\":1, \"a2\":2, \"c\":3}, \"b\":{\"b1\":2, \"b2\":4, \"c\":9}}\n",
        "df = pd.DataFrame(d)"
      ],
      "metadata": {
        "id": "cG8lx_KxSGT_"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"The DataFrame\")\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ttk6tdUoSIPE",
        "outputId": "4430689b-44e6-46ca-9240-24547d22828c"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The DataFrame\n",
            "   a  b\n",
            "0  1  2\n",
            "1  2  4\n",
            "2  3  6\n",
            "3  4  8\n"
          ]
        }
      ]
    }
  ]
}