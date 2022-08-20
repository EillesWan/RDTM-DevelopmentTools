def TSTXTSlice(OpenTXT,Inputlist):
    for TXTSliceErgodic in OpenTXT:
        if '\n' in TXTSliceErgodic:
            Inputlist.append(TXTSliceErgodic[:-1:])
        else:
            Inputlist.append(TXTSliceErgodic)
