import pandas as pd
import numpy as np
import re
from styleframe import StyleFrame
import random


def func01():
    sheet_range = [22]
    df_origin = pd.DataFrame()

    for num in sheet_range:
        excel_sheet_name = re.sub('00', str(num), 'day00')
        df_origin = df_origin.append(pd.read_excel("data/vocabulary.xlsx", sheet_name=excel_sheet_name, header=None), ignore_index=True)

    shuffled_df = df_origin.iloc[np.random.permutation(df_origin.index)].reset_index(drop=True)
    shuffled_df_len = len(shuffled_df.index)
    df_origin = pd.DataFrame(index=[1, 2, 3, 4])
    df_quiz = pd.DataFrame(index=[1, 2, 3, 4])
    for num in range(0, shuffled_df_len, 2):
        df_origin.loc[int(num/2), 1] = shuffled_df.loc[num, 0]
        df_origin.loc[int(num/2), 2] = shuffled_df.loc[num, 1]
        df_origin.loc[int(num/2), 3] = shuffled_df.loc[num+1, 0]
        df_origin.loc[int(num/2), 4] = shuffled_df.loc[num+1, 1]

        seed = random.choice(['VOCA', 'MEANING'])
        if seed == 'VOCA':
            df_quiz.loc[int(num/2), 1] = shuffled_df.loc[num, 0]
            df_quiz.loc[int(num/2), 2] = ''
        elif seed == 'MEANING':
            df_quiz.loc[int(num/2), 1] = ''
            df_quiz.loc[int(num/2), 2] = shuffled_df.loc[num, 1]
        seed = random.choice(['VOCA', 'MEANING'])

        if seed == 'VOCA':
            df_quiz.loc[int(num/2), 3] = shuffled_df.loc[num+1, 0]
            df_quiz.loc[int(num/2), 4] = ''
        elif seed == 'MEANING':
            df_quiz.loc[int(num/2), 3] = ''
            df_quiz.loc[int(num/2), 4] = shuffled_df.loc[num+1, 1]

    excel_writer = StyleFrame.ExcelWriter('data/vocabulary_quiz.xlsx')
    sf_origin = StyleFrame(df_origin)
    sf_quiz = StyleFrame(df_quiz)
    # sf.set_row_height(rows=[n for n in range(1, math.ceil(shuffled_df_len/2)+1)], height=)
    sf_origin.set_row_height(rows=[n for n in range(1, round(shuffled_df_len/2)+1)], height=22.0)
    sf_quiz.set_row_height(rows=[n for n in range(1, round(shuffled_df_len/2)+1)], height=22.0)

    sf_origin.set_column_width(columns=['A', 'C'], width=16.0)
    sf_origin.set_column_width(columns=['B', 'D'], width=40.0)
    sf_quiz.set_column_width(columns=['A', 'C'], width=16.0)
    sf_quiz.set_column_width(columns=['B', 'D'], width=40.0)

    sf_origin.to_excel(excel_writer, header=False, index=False, sheet_name='origin')
    sf_quiz.to_excel(excel_writer, header=False, index=False, sheet_name='quiz')
    excel_writer.save()
