def number_of_lines():
    line_count=0
    fhand = open('mbox-short.txt','r') 
    ff_line = fhand.readlines()[:]
    for i in ff_line:
            line_count+=1
    print(line_count)

def count_number_of_lines():
    fhand = open('mbox-short.txt','r')
    sub_count = 0
    for i in fhand:
        if i.startswith("Subject: "):
            sub_count+=1
    print(sub_count)

def average_spam_confidence():
    fhand = open('mbox-short.txt','r')
    s_count=0
    s_sum=0
    spam_confidence = []
    for i in fhand:
        if i.startswith("X-DSPAM-Confidence: "):
            split_line = i.split(":")
            c_value = float(split_line[1])
            s_sum=s_sum+c_value
            spam_confidence.append(c_value)
            s_count+=1
    print(s_sum / s_count)

def find_email_sent_days():
    days_of_week = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0}
    fhand = open('mbox-short.txt','r')
    for i in fhand:
        if i.startswith("From "):
            words = i.strip().split()
            if len(words) >= 3:
                day = words[2]
                if day in days_of_week:
                    days_of_week[day] += 1
    days_of_week = {k: v for k, v in days_of_week.items() if v > 0}
    print(days_of_week)

def count_message_from_email():
    e_counts = {}
    fhand = open('mbox-short.txt','r')
    for i in fhand:
        if i.startswith("From "):
            words = i.strip().split()
            if len(words) >= 2:
                email = words[1]
                if email in e_counts:
                    e_counts[email] += 1
                else:
                    e_counts[email] = 1
    print(e_counts)

def count_message_from_domain():
    d_counts = {}
    fhand = open('mbox-short.txt','r')
    for i in fhand:
        if i.startswith("From "):
            words = i.strip().split()
            if len(words) >= 2:
                email = words[1]
                domain = email.split('@')[-1]
                if domain in d_counts:
                    d_counts[domain] += 1
                else:
                    d_counts[domain] = 1
    print(d_counts)



number_of_lines()
count_number_of_lines()
average_spam_confidence()
find_email_sent_days()
count_message_from_email()
count_message_from_domain()