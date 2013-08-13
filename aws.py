import boto.ec2
import eisenhower 
import argparse 


#launches and waits for instances to starting running, returns list of public ips
def aws(num_instances,ami_id,securty_group,key_name):
	conn = boto.ec2.connect_to_region("us-east-1")
	res = ec2.conn.run_instances(
        ami_id,
        key_name=key_name,
        instance_type='m1.large',
        security_groups=[security_group],
        min_count=1,
        max_count=num_instances)

	instances = res.instances
	public_ips = ()
	for instance in instances:
		while (instance.state != 'running'):
			time.sleep(10)
		public_ips.append(instance.public_dns_name)
	return public_ips

def main():
  #AWS section
  parser = argparse.ArgumentParser(description='Specifiy the command line arguments to run')
  parser.add_argument('--security',)
  #need to add command line args
  instances = aws(num_instances,ami_id,security_group,key_name)

  # need to shutdown each instance
  #eisenhower section
  closure_test = "Jeremy"
  
  def job(environ):
    import time
    for i in xrange(0, 10):
      time.sleep(1)
      print "%s | Hello, %s!" % (environ['current_host'], closure_test)
    return 42
  
  eisenhower.execute(job, hosts = [ instances ]) #should be 'ssh://each_instance'

if __name__ == '__main__':
  main()
