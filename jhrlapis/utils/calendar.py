from datetime import date,timedelta


class Calender:
    CRLF = "\n"
    SPACE = " "
    CALENDER = {
        'PRODID':'CHNG@ZJUT | CURRICULUM ICS | BY: https://chng.fun/',
        'VERSION':'2.0',
        'CALSCALE':'GREGORIAN',
        'TIMEZONE':'Asia/Shanghai',
        'ISVALARM':True,
        'VALARM':'-P0DT0H15M0S',
        'WKST':'SU',
        'StartDate':'2020-03-02'
    }
    O = []


    def setStartDate(self,startDate):
        self.CALENDER['StartDate'] = startDate


    def getTime(self,num, startOrEnd):
        return [["0600", "0700"], ["0800", "0845"], ["0855", "0940"], ["0955", "1040"], ["1050", "1135"], ["1145", "1230"],
                ["1330", "1415"], ["1425", "1510"], ["1525", "1610"], ["1620", "1705"], ["1830", "1915"], ["1925", "2010"],
                ["2020", "2105"]][num][startOrEnd] + '00';


    def getDate(self, num, wk):
        d = date.fromisoformat(self.CALENDER['StartDate']) + timedelta(days=( (num - 1) * 7 + wk - 1) )
        res = d.strftime('%Y%m%d')
        res += "T"
        return res


    def getWeekName(self,wk):
        return ['MO','TU','WE','TH','FR','SA','SU'][wk-1]


    def fomateCalender(self,raws):
        self.O.clear()
        self.O.append('BEGIN:VCALENDAR')
        self.O.append('VERSION:'+self.CALENDER['VERSION'])
        self.O.append('PRODID:'+self.CALENDER['PRODID'])
        self.O.append('CALSCALE:'+self.CALENDER['CALSCALE'])
        self.O.append(self.CRLF)
        maxWeek = 0
        for row in raws:
            if row['endWeek'] > maxWeek:
                maxWeek = row['endWeek']
            self.O.append('BEGIN:VEVENT')
            self.O.append('DTSTART:' + self.getDate(row['startWeek'],row['week']) + self.getTime(row['startTime'],0));
            self.O.append('DTEND:' + self.getDate(row['startWeek'], row['week']) + self.getTime(row['endTime'], 1));
            self.O.append('RRULE:FREQ=WEEKLY;WKST='+self.CALENDER['WKST']+';COUNT='+str(int((row['endWeek']-row['startWeek']+row['isDouble']+1)/(row['isDouble']+1)))+';INTERVAL='+str(row['isDouble']+1)+';BYDAY='+self.getWeekName(row['week']))
            self.O.append('SUMMARY:'+row['name'])
            self.O.append('LOCATION:'+row['location']+' '+row['teacher'])
            if self.CALENDER['ISVALARM']:
                self.O.append('BEGIN:VALARM')
                self.O.append('ACTION:DISPLAY')
                self.O.append('DESCRIPTION:上课提醒')
                self.O.append('TRIGGER:' + self.CALENDER['VALARM'])
                self.O.append('END:VALARM')
            self.O.append('END:VEVENT')
            self.O.append(self.CRLF)

        for i in range(0,maxWeek):
            self.O.append('BEGIN:VEVENT')
            self.O.append('DTSTART:' + self.getDate(i+1,1) + self.getTime(0,0))
            self.O.append('DTEND:' + self.getDate(i + 1, 1) + self.getTime(0, 1))
            self.O.append('SUMMARY:第' + str(i+1) + '周')
            self.O.append('END:VEVENT')
            self.O.append(self.CRLF)

        self.O.append('END:VCALENDAR')

        return self.O


    def getIcs(self):
        res = ''
        for row in self.O:
            lent = len(row)
            if lent > 60:
                ind = 0
                while lent>0:
                    for i in range(0,ind):
                        res += self.SPACE
                    res += row[0:60]
                    res += self.CRLF
                    row = row[61:lent]
                    lent -= 60
                    ind+=1
                row = row[0:60]
            res += row + self.CRLF
        return res