
info = []
daily_time=0
other_time=0

with open(r'C:\Users\drews\SZvsWorkspace\PersonalProjects\MessingAbout\hour_calc\time_catalog.txt','r') as f:
    for line in f:
        if str(line[0]) == '.':
            time,subject = line.split('.')[1].split(' ')[:2]
            start_hour,start_min,end_hour,end_min = time.replace('-',':').split(':')
            
            if int(start_hour) > int(end_hour):
                total_time = 60*(int(end_hour) + 12 - int(start_hour)) +(int(end_min)-int(start_min))
            else:
                total_time = 60*(int(end_hour)-int(start_hour))+(int(end_min)-int(start_min))
            
            info.append([subject,total_time])
            daily_time += int(total_time)
        else:
            try:
                int(line[0])
                time = line.split(' ')[0]
                start_hour,start_min,end_hour,end_min = time.replace('-',':').split(':')
                if int(start_hour) > int(end_hour):
                    other_total_time = 60*(int(end_hour) + 12 - int(start_hour)) +(int(end_min)-int(start_min))
                else:
                    other_total_time = 60*(int(end_hour)-int(start_hour))+(int(end_min)-int(start_min))
                other_time += int(other_total_time)

            except ValueError:
                pass
total = daily_time + other_time

lines = []

print('-+-===============-+-')
lines.append('-+-===============-+-')
for i in range(len(info)):
    print(f'| {info[i][0]} - {int(info[i][1]/60)}h {60*(info[i][1]/60-int(info[i][1]/60)):.0f}m')
    lines.append(f'\n| {info[i][0]} - {int(info[i][1]/60)}h {60*(info[i][1]/60-int(info[i][1]/60)):.0f}m')

print('-+-===============-+-')
lines.append('\n-+-===============-+-')
print(f'| Study: {int(daily_time/60)}h {60*(daily_time/60-int(daily_time/60)):.0f}m')
lines.append(f'\n| Study: {int(daily_time/60)}h {60*(daily_time/60-int(daily_time/60)):.0f}m')
print(f'| Total: {int(total/60)}h {60*(total/60-int(total/60)):.0f}m')
lines.append(f'\n| Total: {int(total/60)}h {60*(total/60-int(total/60)):.0f}m')
print('-+-----------------+-')
lines.append('\n-+-----------------+-')
lines.append('\n\n'+r'cd C:\Users\drews\SZvsWorkspace\PersonalProjects\MessingAbout\hour_calc')
lines.append('\npython hour_calculator.py')
with open(r'C:\Users\drews\SZvsWorkspace\PersonalProjects\MessingAbout\hour_calc\time_catalog.txt', "r+") as fp:
    fp.truncate(0)
with open(r'C:\Users\drews\SZvsWorkspace\PersonalProjects\MessingAbout\hour_calc\time_catalog.txt','w') as file:
    file.writelines(lines)
