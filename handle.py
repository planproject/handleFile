import configparser


cfg = configparser.ConfigParser()
cfg.read('find.txt')

# help(cfg.sections());

# print(cfg.sections())   #打印 [session] 值


cfg.set('userinfo', 'name', 'FerreWagner');
cfg.set('userinfo', 'hate', 'FerreWagner');
cfg.remove_option('userinfo', 'hate')


for se in cfg.sections():
    print(se)
    print(cfg.items(se))