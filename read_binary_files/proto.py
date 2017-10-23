from struct import *
import os

filename = "txnlog.dat"
header = []

def unpack_file_header(header):
    with open(filename, "rb") as f:
        buffer = f.read()
        strformat = ">4c B I"
        unpacked = unpack_from(strformat, buffer)
        magic_string = ""
        for i in unpacked[:4]:
            magic_string += i
        header.append(magic_string)
        header.append(unpacked[4])
        header.append(unpacked[5])
        return header

header = unpack_file_header(header)
print "Header found:",header


def unpack_records(header):
    records = []
    # Keep track of the byte position as we progress.
    position = 9
    with open(filename, "rb") as f:
        # Skip the file header
        f.seek(position)
        for i in range(header[2]):
            # Get the record type
            buffer = f.read(1)
            position += 1
            record = []
            rtype = unpack_from("b", buffer)[0]
            record.append(rtype)
            # Optional float amount if record type 0 or 1.
            if rtype in [0,1]:
                buffer = f.read(20)
                unpacked = unpack_from(">I Q d", buffer)
                for i in unpacked: record.append(i)
            else:
                buffer = f.read(12)
                unpacked = unpack_from(">I Q", buffer)
                for i in unpacked: record.append(i)
            records.append(record)
    return records

records = unpack_records(header)
print "Records parsed:",len(records)
print


# What is the total amount in dollars of debits?
def calc_total_debits(records):
    total = 0.0
    for record in records:
        if record[0] == 0:
            total += record[3]
    return total

total_debits = calc_total_debits(records)
print "Total amount in dollars of debits:",total_debits


# What is the total amount in dollars of credits?
def calc_total_credits(records):
    total = 0.0
    for record in records:
        if record[0] == 1:
            total += record[3]
    return total

total_credits = calc_total_credits(records)
print "Total amount in dollars of credits:",total_credits


# How many autopays were started?
def calc_start_autopays(records):
    num_start_autopay = 0
    for record in records:
        if record[0] == 2:
            num_start_autopay += 1
    return num_start_autopay

total_start_autopay = calc_start_autopays(records)
print "Autopays started:",total_start_autopay


# How many autopays were ended?
def calc_end_autopays(records):
    num_end_autopay = 0
    for record in records:
        if record[0] == 3:
            num_end_autopay += 1
    return num_end_autopay

total_end_autopay = calc_end_autopays(records)
print "Autopays ended:",total_end_autopay


# What is balance of user ID 2456938384156277127?
def calc_user_balance(user):
    balance = 0.0
    for record in records:
        if record[2] == user:
            if record[0] == 0:
                balance -= record[3]
            elif record[0] == 1:
                balance += record[3]
            else:
                pass
    return balance

user = 2456938384156277127
user_balance = calc_user_balance(user)
print "User ID %s balance: %s" % (user,user_balance)
