
#!/usr/bin/python
import boto3
import sys
import string
session = boto3.session.Session(profile_name='alpha_gov_prod')
elb_name = "****"
client = session.client('elbv2')

response = client.describe_target_groups(
    LoadBalancerArn=elb_name
)

for item in response['TargetGroups']:
#  print (item['TargetGroupArn'])
  if 'tfgreenpilot-dp' in  (item['TargetGroupArn']):
    print(item['TargetGroupArn'])
    print('---tfgreenpilot-dp---')
#   response = client.register_targets(
#      TargetGroupArn=(item['TargetGroupArn']),
#      Targets=[
#        {
#            'Id': 'i-0a49fa95060c07f14',
#        },
#        {
#            'Id': 'i-0a6ff7755a2a61f00',
#        },
#       ],
#       )
for item in response['TargetGroups']:
  if 'tfgreenpilot-analytics' in  (item['TargetGroupArn']):
      print(item['TargetGroupArn'])
      print('---tfgreenpilot-analytics---')
#      response = client.register_targets(
#      TargetGroupArn=(item['TargetGroupArn']),
#      Targets=[
#          {
#              'Id': 'i-0fe535a9ba3b2eefe',
#          }
#          ],
#          )
  elif 'tfgreenpilot-dvs' in  (item['TargetGroupArn']):
     print(item['TargetGroupArn'])
     print ("----------tfgreenpilot-dvs----------")
#      response = client.register_targets(
#       TargetGroupArn=(item['TargetGroupArn']),
#      Targets=[
#          {
#              'Id': 'i-0f82dce8b9a1570ba',
#          }
#          ],
#          )


  elif 'tfgreenpilot-tipm-443' in  (item['TargetGroupArn']):
     print(item['TargetGroupArn'])
     print('----------tfgreenpilot-tipm-443--------')
#      response = client.register_targets(
#      TargetGroupArn=(item['TargetGroupArn']),
#      Targets=[
#          {
#              'Id': 'i-0f82dce8b9a1570ba',
#          }
#          ],
#          )
  else:
    print(item['TargetGroupArn'])
    response = client.register_targets(
      TargetGroupArn=(item['TargetGroupArn']),
      Targets=[
          {
              'Id': 'i-09cace99a15db8fbc',
          }
          ],
          )
