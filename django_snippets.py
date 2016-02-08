request_counts = 0
years = [2013,2014,2015]
import calendar
for year in years:
    for month in range(1,13):
        print "Date: %s %r" % (month, year)
        monthrange = calendar.monthrange(year,month)
        start_datetime = datetime(year, month, 01, 0, 0, 0, 0)
        end_datetime = datetime(year, month, monthrange[1], 23, 59, 59, 999999)

        foo = Request.objects.filter(
            deleted__isnull = True, template__in = template_ids, is_template = 0).filter(
            cur_stage__completed__gte=start_datetime, cur_stage__completed__lte=end_datetime
        )
        print len(foo)
        request_counts += len(foo)

"""
Date: 1 2013
11
Date: 2 2013
3
Date: 3 2013
5
Date: 4 2013
10
Date: 5 2013
10
Date: 6 2013
4
Date: 7 2013
1
Date: 8 2013
60
Date: 9 2013
16
Date: 10 2013
0
Date: 11 2013
5
Date: 12 2013
3
Date: 1 2014
33
Date: 2 2014
1
Date: 3 2014
0
Date: 4 2014
4
Date: 5 2014
34
Date: 6 2014
67
Date: 7 2014
0
Date: 8 2014
6
Date: 9 2014
39
Date: 10 2014
0
Date: 11 2014
1
Date: 12 2014
3
Date: 1 2015
2
Date: 2 2015
0
Date: 3 2015
0
Date: 4 2015
0
Date: 5 2015
0
Date: 6 2015
0
Date: 7 2015
0
Date: 8 2015
0
Date: 9 2015
0
Date: 10 2015
0
Date: 11 2015
0
Date: 12 2015
0
"""

from tbd.models import Request as Req
import calendar

request_counts = 0
years = [2013,2014,2015]
for year in years:
    for month in range(1,13):
        print "Date: %s %r" % (month, year)
        monthrange = calendar.monthrange(year,month)
        start_datetime = datetime(year, month, 01, 0, 0, 0, 0)
        end_datetime = datetime(year, month, monthrange[1], 23, 59, 59, 999999)

        # import ipdb; ipdb.set_trace()
        foo = Req.objects.filter(
            deleted=0,
            tags=35,
            current_step__completed__gte=start_datetime,
            current_step__completed__lte=end_datetime
        )
        print len(foo)
        request_counts += len(foo)
"""
Date: 1 2013
0
Date: 2 2013
0
Date: 3 2013
0
Date: 4 2013
0
Date: 5 2013
0
Date: 6 2013
0
Date: 7 2013
0
Date: 8 2013
0
Date: 9 2013
0
Date: 10 2013
0
Date: 11 2013
0
Date: 12 2013
0
Date: 1 2014
0
Date: 2 2014
0
Date: 3 2014
0
Date: 4 2014
0
Date: 5 2014
0
Date: 6 2014
0
Date: 7 2014
0
Date: 8 2014
0
Date: 9 2014
0
Date: 10 2014
0
Date: 11 2014
0
Date: 12 2014
0
Date: 1 2015
7
Date: 2 2015
20
Date: 3 2015
0
Date: 4 2015
0
Date: 5 2015
27
Date: 6 2015
6
Date: 7 2015
2
Date: 8 2015
31
Date: 9 2015
37
Date: 10 2015
16
Date: 11 2015
0
Date: 12 2015
28
"""