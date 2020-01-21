
import pandas as pd
import re
import os
import datetime
import shutil

def customDataCleaningForIR56B(workflow_Excel_path, cwd):

    output_final = pd.read_excel(workflow_Excel_path, sheet_name=3)
    output_final.rename(columns={"NOTIFICATION":"Nature of the form (Original/Revised/Additional)","Employer's File No.:": "Employer's File No","Name of Employer:": "Name of Employer","H.K. Identity Card Number:":'Taxpayer HKID card',"Surname of Employee or Pensioner:": 'Taxpayer Last Name', "Salaries Tax Paid by Employer":'Salaries Tax Paid by Employer',
                                 'Given name in Full:':'Taxpayer Given name in Full',"Spouse's H.K. Identity Card Number:":"Spouse HKID card", "If married, full name of spouse:":"Spouse Name","Residential address_person:":'Residential address',
                                 "Capacity in which employed:":'Capacity',"(a) Address 1:":"Address 1", "Period of employment for the year from 1 April 2018 to 31 March 2019:": "Period of employment",
                                 "by a non-Hong Kong company: (0=No, 1=Yes)":'Whether the employee was wholly or partly paid either in Hong Kong or elsewhere','Period Provided:':'Period 1',
                                 "Passport Number and place of issue:":'Taxpayer Passport Number and place of issue',"Marital status (1=Single/Widowed/Divorced/Living Apart, 2=Married):":"Marital status",
                                 'Rent paid to Landlord by Employer': 'Address 1 Rent paid to Landlord by Employer',"Sex (M=Male, F=Female):":'Taxpayer Gender',"Any Other Rewards Allowances or Perquisites":'Any Other Rewards or Allowances or Perquisites',
                                 'Rent paid to Landlord by Employee:': 'Address 1 Rent paid to Landlord by Employee','Postal Address (if different from 7 above):':"Postal Address","If part time, the name of his/her principal employer (if known):":"Part time employer name",
                                 'Rent Refunded to Employee by Employer': 'Address 1 Rent Refunded to Employee by Employer','Back pay, Payment in Lieu of Notice, Terminal Awards or Gratuities':'Back Pay, Payment in Lieu of Notice, Terminal Awards or Gratuities',
                                 'Rent Paid to Employer by Employee': 'Address 1 Rent Paid to Employer by Employee','Particulars of Place of Residence provided: (0=Not provided, 1=Provided)':'Particulars of Place of Residence provided:',
                                 'Nature1: Cash / housing allowance':"Nature 1","Spouse's Passport Number and place of issue (if known):":"Passport Number and place of issue:",
                                 "Nature2: Other allowance / award":"Nature 2","(b) Address 2:":"Address Place of residence provided 2","Director's Fees":"Director's Fee",
                                 "Nature3: Foreign Individual Income Tax paid by Employer": "Nature 3",
                                 '(a) Address 1:':'Address Place of residence provided 1',
                                 'Nature:':'Nature_1',"Total:":"Total income",
                                 "Rent paid to Landlord by Employer:":"Rent paid by employer 1",
                                 "Rent paid to Landlord by Employee:":"Rent paid by employee 1",
                                 "Rent Refunded to Employee by Employer:":"Rent refunded to employee by employer 1",
                                 "Rent Paid to Employer by Employee:":"Rent paid by employee to employer 1",
                                 'Name of the non-Hong Kong company:':'Name of the non-Hong Kong company',
                                 "Address:" :"Non-Hong Kong company Address",
                                 "Amount (if known) (This amount must also be included in item 11):":"Amount paid overseas non-Hong Kong company",
                                 "Remarks:":"Remarks"


                                                             }, inplace=True)

    output_final["Type of the Form (56B/56G/56F/56M)"] = "56B"

    form_type = output_final["Nature of the form (Original/Revised/Additional)"].to_string()
    if form_type is not None:
        try:
            output_final["Nature of the form (Original/Revised/Additional)"] = output_final[
                "Nature of the form (Original/Revised/Additional)"].apply(
                lambda x: ('Additional' if 'additional' in x else "Original") or (
                    'Revised' if 'revised' in x else "Original"))
        except:
            output_final["Nature of the form (Original/Revised/Additional)"] = "Original"

    hk_no = output_final["Taxpayer HKID card"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Taxpayer HKID card"] = hk_no.apply(lambda x: str(x).replace("*", ""))

    output_final["Employer's File No"] = output_final["Employer's File No"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Taxpayer Given name in Full"] = output_final["Taxpayer Given name in Full"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))

    tax_player_name = output_final["Taxpayer Last Name"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Taxpayer Last Name"] = tax_player_name.apply(lambda x: str(x).replace("*", ""))

    output_final["Taxpayer Tax file number"] = ""

    output_final["Taxpayer Passport Number and place of issue"] = output_final[
        "Taxpayer Passport Number and place of issue"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))


    tax_gender = output_final["Taxpayer Gender"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(' '))
    output_final["Taxpayer Gender"]= tax_gender.apply(lambda x: str(x).replace("*", ""))


    output_final["Marital status"] = output_final["Marital status"].apply(
        lambda x: str(x).replace("*", "").lstrip())
    output_final["Name of Employer"] = output_final["Name of Employer"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Address of Employer"] = ''
    output_final["Residential address"] = output_final["Residential address"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Postal Address"] = output_final[
        "Postal Address"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Capacity"] = output_final["Capacity"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Part time employer name"] = ''
    output_final["Expected cessation date"] =''


    output_final["Spouse HKID card"] = output_final["Spouse HKID card"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Passport Number and place of issue:"] = output_final["Passport Number and place of issue:"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Spouse Name"] = output_final["Spouse Name"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))

    output_final["Reason for cessation"] = ''
    sal_peroid = output_final["Period of employment"]

    try:

        for salary_peroid in sal_peroid:
            if str(salary_peroid) == 'nan':

                p_val = output_final["Salary/Wages"].apply(lambda x: str(x).split()[0]) + " to " + output_final[
                    "Salary/Wages"].apply(lambda x: str(x).split()[2])
                output_final['Period of employment'] = output_final[
                    'Period of employment'].fillna(p_val)
            else:
                output_final['Period of employment'] = sal_peroid
    except:
        print("Error")


    if output_final["Salary/Wages"] is not None:
        sal = output_final["Salary/Wages"].to_string()
        if sal is not None:
            sal_data = output_final["Salary/Wages"].apply(lambda x: str(x).split()[-1])

            output_final["Salary/Wages"] = sal_data
    if output_final['Salaries Tax Paid by Employer'] is not None:

        sal_tax = output_final["Salaries Tax Paid by Employer"].to_string()
        if sal_tax is not None:
            sal_tax_data = output_final["Salaries Tax Paid by Employer"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Salaries Tax Paid by Employer"] = sal_tax_data

    if output_final['Leave Pay'] is not None:

        sal_tax = output_final["Leave Pay"].to_string()
        if sal_tax is not None:
            sal_tax_data = output_final["Leave Pay"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Leave Pay"] = sal_tax_data

    if output_final['Commission/Fees'] is not None:

        sal_tax = output_final["Commission/Fees"].to_string()
        if sal_tax is not None:
            sal_tax_data = output_final["Commission/Fees"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Commission/Fees"] = sal_tax_data
    if output_final['Bonus'] is not None:

        bon_tax = output_final["Bonus"].to_string()
        if bon_tax is not None:
            bon_tax_data = output_final["Bonus"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Bonus"] = bon_tax_data

    if output_final["Back Pay, Payment in Lieu of Notice, Terminal Awards or Gratuities"] is not None:

        sal_tax = output_final["Back Pay, Payment in Lieu of Notice, Terminal Awards or Gratuities"].to_string()
        if sal_tax is not None:
            sal_tax_data = output_final["Back Pay, Payment in Lieu of Notice, Terminal Awards or Gratuities"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Back Pay, Payment in Lieu of Notice, Terminal Awards or Gratuities"] = sal_tax_data

    if output_final['Gain realized under Share Option Scheme'] is not None:
        gain_realized = output_final["Gain realized under Share Option Scheme"].to_string()
        if gain_realized is not None:
            gain_realized_amt = output_final["Gain realized under Share Option Scheme"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Gain realized under Share Option Scheme"] = gain_realized_amt
    if output_final["Any Other Rewards or Allowances or Perquisites"] is not None:
        gain_Allowances = output_final["Any Other Rewards or Allowances or Perquisites"].to_string()
        if gain_Allowances is not None:
            gain_Allowances_amt = output_final["Any Other Rewards or Allowances or Perquisites"].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final["Any Other Rewards or Allowances or Perquisites"] = gain_Allowances_amt

    if output_final['Nature 1'] is not None:
        nature = output_final['Nature 1'].to_string()
        if nature is not None:
            nature_amount = output_final['Nature 1'].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final['Nature 1'] = nature_amount
        else:
            output_final['Nature 1'] = ''

    output_final["Total income"] = output_final["Total income"].apply(lambda x: str(x).replace("*", ""))



    if output_final['Nature 2'] is not None:

        nature2 = output_final['Nature 2'].to_string()
        if nature2 is not None:
            nature2_amount = output_final['Nature 2'].apply(lambda x: str(x).split()[-1]if (str(x) != 'nan') else str(''))
            output_final['Nature 2'] = nature2_amount

    if output_final['Nature 3'] is not None:

        nature3 = output_final['Nature 3'].to_string()
        if nature3 is not None:
            nature3_amount = output_final['Nature 3'].apply(
                lambda x: str(x).split()[-1] if (str(x) != 'nan') else str(''))
            output_final['Nature 3'] = nature3_amount

    output_final['Pensions'] = ""


    output_final["Payments that have not been declared above but which will be made"] = ''

    output_final["Particulars of Place of Residence provided:"] = output_final[
        "Particulars of Place of Residence provided:"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Particulars of Place of Residence provided:"] = output_final[
        "Particulars of Place of Residence provided:"].apply(lambda x: str(x).replace("*", ""))

    output_final["Address Place of residence provided 1"] = output_final["Address Place of residence provided 1"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan')else str(''))
    try:
        addrees_nature = output_final["Nature_1"].astype(str).apply(
            lambda x: str(x).split("period")[0] if ("period" in str(x)) else str(x))
        output_final["Nature_1"] = addrees_nature.apply(
            lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    except:
        output_final["Nature_1"] = ""

    output_final["Period 1"] =output_final['Period of employment']

    output_final['Rent paid by employer 1'] = output_final[
        'Rent paid by employer 1'].astype(str).apply(
        lambda x: str(x).replace("hk$", "").replace("nan", "") if (", " or "nan" in str(x)) else str(x))

    output_final['Rent paid by employee 1'] = output_final[
        'Rent paid by employee 1'].astype(str).apply(
        lambda x: str(x).replace("hk$", "").replace("nan", "") if (", " or "nan" in str(x)) else str(x))

    output_final['Rent refunded to employee by employer 1'] = output_final[
        'Rent refunded to employee by employer 1'].astype(str).apply(
        lambda x: str(x).replace("hk$", "").replace("nan", "") if (", " or "nan" in str(x)) else str(x))

    output_final['Rent paid by employee to employer 1'] = output_final[
        'Rent paid by employee to employer 1'].astype(str).apply(
        lambda x: str(x).replace("hk$", "").replace("nan", "") if (", " or "nan" in str(x)) else str(x))

    output_final["Address Place of residence provided 2"] = ""
    output_final["Nature_2"] = ""

    output_final["Period 2"] = ""
    output_final['Rent paid by employer 2'] = ""

    output_final['Rent paid by employee 2'] = ""
    output_final['Rent refunded to employee by employer 2'] = ""

    output_final['Rent paid by employee to employer 2'] = ""

    output_final["Address Place of residence provided 3"] = ""
    output_final["Nature_3"] = ""

    output_final["Period 3"] = ""
    output_final['Rent paid by employer 3'] = ""

    output_final['Rent paid by employee 3'] = ""
    output_final['Rent refunded to employee by employer 3'] = ""

    output_final['Rent paid by employee to employer 3'] = ""

    hk_else = output_final["Whether the employee was wholly or partly paid either in Hong Kong or elsewhere"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))
    output_final["Whether the employee was wholly or partly paid either in Hong Kong or elsewhere"] = hk_else.apply(
        lambda x: str(x).replace("*", ""))

    output_final["Name of the non-Hong Kong company"] = output_final["Name of the non-Hong Kong company"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))

    output_final["Non-Hong Kong company Address"] = output_final["Non-Hong Kong company Address"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))

    output_final['Amount paid overseas non-Hong Kong company'] = output_final[
        'Amount paid overseas non-Hong Kong company'].astype(str).apply(
        lambda x: str(x).replace(": hk$", "").replace("nan", "") if (", " or "nan" in str(x)) else str(x))

    output_final['Future Postal address'] =''

    output_final['Tax borne'] = ""
    output_final['Money withheld amount'] = ""

    output_final['No Money withheld Reason'] = ""
    output_final['Reason for departure'] = ""

    output_final['Will return to Hong Kong'] = ""
    output_final['Number Unvested shares'] = ""
    output_final['Grant date of unvested shares'] = ""
    output_final["Remarks"] = output_final["Remarks"].apply(
        lambda x: str(x).upper().lstrip() if (str(x) != 'nan') else str(''))

    output_final["Status"] = ""

    output_final["Exception Details"] = ""

    # current_directory = os.getcwd()
    #
    # timestamp = datetime.datetime.now()
    # dt = str(timestamp.year) + str(timestamp.month) + str(timestamp.day) + str(timestamp.hour) + str(timestamp.minute)
    # newname = 'IR56B_TypeII_' + str(dt) + '.xlsx'
    # output_path = os.path.join(current_directory + '/Output_File', newname)
    # print("Generate output excel to ", output_path)
    # output_final.to_excel(output_path, index=False)
    return output_final