import xlrd,xlwt,os,xlsxwriter,random

#######################Random data generator##########################
import string, random
def data_generator(data=9999, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(data))
data_generator(1000)
######################################################################

def GetFileList(path):
    list = []
    for dirPath, dirNames, fileNames in os.walk(path):
        for f in fileNames:
            list.append(os.path.join(dirPath, f))
    return list

class RdExcel:
    def __init__(self,file):
        self.file = file
        self.data = xlrd.open_workbook(self.file)
        self.NameList = self.data.sheet_names()
    def GetRowsCount(self,SheetIdx):
        sh = self.data.sheet_by_index(SheetIdx)
        return sh.nrows
    def GetColsCount(self,SheetIdx):
        sh = self.data.sheet_by_index(SheetIdx)
        return sh.ncols
    def GetRowsVal(self,SheetIdx,row):
        sh = self.data.sheet_by_index(SheetIdx)
        val = sh.row_values(row)
        return val
    def GetColsVal(self,SheetIdx,col):
        sh = self.data.sheet_by_index(SheetIdx)
        val = sh.row_values(col)
        return val
    def GetCellVal(self,SheetIdx,col,row):
        sh = self.data.sheet_by_index(SheetIdx)
        val = str(sh.cell(col,row))
        vallist = val.split(':')
        return vallist
    def __str__(self):
        return '{0},{1},{2}'.format(self.file,self.data,self.NameList)

# file = 'test.xlsx'
# form = RdExcel(file)
# form.GetRowsCount(0)
# form.GetColsCount(0)
# form.GetRowsVal(0,0)
# form.GetRowsVal(0,1)
# form.GetRowsVal(0,2)
# form.GetColsVal(0,0)
# form.GetColsVal(0,1)
# form.GetColsVal(0,2)
# form.GetCellVal(0,0,0)

class WrExcel:
    def __init__(self,filename):
        self.wb = xlsxwriter.Workbook(filename+'.xlsx')
    def AddSheet(self,name=None):
        self.sh = self.wb.add_worksheet(name)
    def Write(self,position,var,format=''):
        if format:self.sh.write(position, var, format)
        else:self.sh.write(position, var)
    def WriteCol(self,position,varlist,format=''):
        if format:self.sh.write_row(position, varlist, format)
        else:self.sh.write_row(position, varlist)
    def WriteRow(self,position,varlist,format=''):
        if format:self.sh.write_column(position, varlist, format)
        else:self.sh.write_column(position, varlist)
    def AddChart(self,type,sheet,title,xasix,yasix,series_list,position):
        AddChart(self.wb,self.sh,type,sheet,title,xasix,yasix,series_list,position)
    def __str__(self):
        return '{0},{1}'.format(self.wb,self.sh)
    def close(self):
        self.wb.close()

def AddSeries(name,categories,value,sheet='Sheet1'):
    xstart = value.split('-')[0]
    xend = value.split('-')[1]
    ystart = categories.split('-')[0]
    yend = categories.split('-')[1]
    series = {
            'name':       '{2}!${0}${1}'.format(name[0],name[1:],sheet),
            'categories': '{4}!${0}${1}:${2}${3}'.format(ystart[0],ystart[1:],yend[0],yend[1:],sheet),
            'values':     '{4}!${0}${1}:${2}${3}'.format(xstart[0],xstart[1:],xend[0],xend[1:],sheet),
        }
    return series

def AddChart(wb,sh,type,sheet,title,xasix,yasix,series_list,position):
    type = type
    sheet = sheet
    # print(xstart,xend,ystart,yend)
    chart = wb.add_chart({'type':type})
    chart.set_title ({'name': title})
    chart.set_x_axis({'name': xasix})
    chart.set_y_axis({'name': yasix})
    for series in series_list:
        chart.add_series(series)
    chart.set_style(11)
    sh.insert_chart(position, chart)
    print('{0},{1},{2},{3},{4}'.format(wb,sh,type,sheet,chart))

b = WrExcel('Nick')
b.AddSheet('yyy')
# b.Write('A1','Nick',bold)
y = []
for q in xrange(80):
    y.append(random.uniform(-2,2))
    
b.WriteCol('A1',['value','Frequency','Low','Up'])
b.WriteRow('A2',y)
print type(y[0])
b.WriteRow('B2',range(5,85))
b.WriteRow('C2',[-2]*80)
b.WriteRow('D2',[2]*80)
SerUp = AddSeries('D1','B2-B81','D2-D81','yyy')
SerLow = AddSeries('C1','B2-B81','C2-C81','yyy')
Diff = AddSeries('A1','B2-B81','A2-A81','yyy')
b.AddChart('line','yyy','test','Frequency','Deff(dB)',[SerUp,SerLow,Diff],'E1')
# b.AddChart('line','Sheet1','Nick test','Number','Frequency','D8')

y = []
for q in xrange(80):
    y.append(random.uniform(-2,2))

b.AddSheet('AAA')
b.WriteCol('A1',['value','Frequency','Low','Up'])
b.WriteRow('A2',y)
print type(y[0])
b.WriteRow('B2',range(5,85))
b.WriteRow('C2',[-2]*80)
b.WriteRow('D2',[2]*80)
SerUp = AddSeries('D1','B2-B81','D2-D81','AAA')
SerLow = AddSeries('C1','B2-B81','C2-C81','AAA')
Diff = AddSeries('A1','B2-B81','A2-A81','AAA')
b.AddChart('line','AAA','test','Frequency','Deff(dB)',[SerUp,SerLow,Diff],'E1')
b.close()