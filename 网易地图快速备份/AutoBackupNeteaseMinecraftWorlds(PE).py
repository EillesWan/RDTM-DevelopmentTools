# -*-coding:utf-8-*-


'''

愿不会再有人受伤
愿这个世界还存在着爱
愿我的一片心意将不被辜负


谨以此程序
赠
百叶Brianna


—— 金羿Eilles 2022 3 25
'''


import os
import hashlib
import shutil


def getFileMd5(filename):
    if not os.path.isfile(filename):
        print('file not exist: ' + filename)
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def getAllFiles(path):
    flist = []
    for root, dirs, fs in os.walk(path):
        for f in fs:
            f_fullpath = os.path.join(root, f)
            f_relativepath = f_fullpath[len(path) :]
            flist.append(f_relativepath)
    return flist


def dirCompare(apath, bpath):
    '''给予两个目录，比较其目录文件异同
    返回True为不同，返回False为完全一致
    '''

    res = False

    afiles = getAllFiles(apath)
    bfiles = getAllFiles(bpath)

    setA = set(afiles)
    setB = set(bfiles)

    commonfiles = setA & setB  # 处理共有文件

    for f in sorted(commonfiles):
        amd = getFileMd5(apath + '\\' + f)
        bmd = getFileMd5(bpath + '\\' + f)
        if amd != bmd:
            # print ("dif file: %s" %(f))
            res = True

    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB
    onlyInA = []
    onlyInB = []
    for of in onlyFiles:
        if of in afiles:
            onlyInA.append(of)
        elif of in bfiles:
            onlyInB.append(of)

    if len(onlyInA) > 0:
        # print ('-' * 20,"only in ", apath, '-' * 20)
        for of in sorted(onlyInA):
            # print (of)
            res = True

    if len(onlyInB) > 0:
        # print ('-' * 20,"only in ", bpath, '-' * 20)
        for of in sorted(onlyInB):
            # print (of)
            res = True

    return res


# 上部分代码摘抄并改编自CSDN用户 林新发 的CSDN博客 https://blog.csdn.net/linxinfa/article/details/90240952


def makepairs(
    path1: str = os.getenv('APPDATA') + '\\MinecraftPE_Netease\\minecraftWorlds',
    path2: str = '.\\backup\\',
):

    rstpaths = []
    rstnames = {}
    pairs = {}
    for filename in os.listdir(path1):
        if '.' in filename:
            continue
        else:
            try:
                int(filename)
                continue
            except:
                rstpaths.append(os.path.join(path1, filename))
                rstnames[rstpaths[-1]] = filename

    for filename in os.listdir(path2):
        if '.' in filename:
            continue
        else:
            try:
                int(filename)
                continue
            except:
                if filename in rstnames.values():
                    pairs[os.path.join(path1, filename)] = os.path.join(path2, filename)

    return rstpaths, pairs, rstnames


if __name__ == '__main__':

    if os.path.exists('./settings.ini'):
        # settings 中用换行隔开，请使用单独的文件夹，里面除了地图以外不要放别的东西。
        bPath = open('./settings.ini', 'r', encoding='utf-8').read()
    else:
        bPath = input('请输入备份文件夹的位置：')
        if not os.path.exists(bPath):
            os.makedirs(bPath)
        isdef = input(
            '如果您备份位置是固定的，建议您将位置写入与程序同目录下的settings.ini中，是否把您刚才输入的位置设定为默认备份位置？ [y/N]'
        ).lower()
        if isdef == 'y':
            open('./settings.ini', 'w', encoding='utf-8').write(bPath)
        elif isdef == 'n':
            pass
        else:
            print('已取消默认位置设定')

    rp, dpdict, rn = makepairs(path2=bPath)

    for path in rp:
        if path in dpdict.keys():
            if dirCompare(path, dpdict[path]):
                shutil.rmtree(dpdict[path])
                shutil.copytree(path, dpdict[path])
        else:
            shutil.copytree(path, os.path.join(bPath, rn[path]))

    print("\ndone!")
