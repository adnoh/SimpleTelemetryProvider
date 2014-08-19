"""
The MIT License (MIT)

Copyright (c) 2014 Moritz Wundke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import config
import traceback
import datetime

def stats_list_to_dict(stats_list):
    stats_dict = {}
    for stats in stats_list:
        try:
            stats_dict[stats["Item1"]] = float(stats["Item2"].replace(',','.'))
        except:
            stats_dict[stats["Item1"]] = stats["Item2"]
    return stats_dict

def insert_event(data):
    try:
        event = {}
        event["sessionid"] = data["sessionid"]

        # Add all stats
        event["BuildStatsTotal"] = stats_list_to_dict(data["BuildStatsTotal.2"])
        event["LoadIncludeDependencyCacheStats"] = stats_list_to_dict(data["LoadIncludeDependencyCacheStats.2"])
        event["PerformanceInfo"] = stats_list_to_dict(data["PerformanceInfo.2"])
        event["CommonAttributes"] = stats_list_to_dict(data["CommonAttributes.2"])
        event["TargetBuildStats"] = stats_list_to_dict(data["TargetBuildStats.2"])

        # Add to DB
        config.DB.events.insert(event)
    except:
        traceback.print_exc()

def listing(**k):
    return config.DB.events.aggregate(
        [
            {
                "$match": { "event" : "BuildStatsTotal.2" }
            },
            
            {
                "$group": {           
                    "_id": {"command": "$cmd", "buildTime": "$data.TotalUBTWallClockTimeSec"}
                }
                
            },
            {
                "$project": {
                    "command": "$_id.command",
                    "buildTime": "$_id.buildTime",            
                    "_id": 0
                }
                    
            },
            {
                "$sort": { 
                    "command": 1
                }
            }
        ]
    )['result']
