emails = ["max.mustermann@example.com",
          "anna.mueller@example.com",
          "peter.pan@example.com"
          "@dscscs.com",
          'sdcds@cdskcscsdkcd@sdwwsd.com',
          'sx.sxs@dasddsad',
          'qwdqdwd.cfd']
for i in range(len(emails)):
    if emails[i].count('@') == 1 and emails[i].split("@")[1].count(".") != 0 and emails[i].index("@") > 0:
        print(f'e-mail: {emails[i]} вірний')
    else:
        print(f'e-mail: {emails[i]} недійсний')