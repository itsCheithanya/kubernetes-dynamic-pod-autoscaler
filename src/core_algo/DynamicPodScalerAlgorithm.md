
Input: predicted_workload  # predicted workload in the next interval in rps
       current_workload   # current workload of the application in rps 
Output: Scale UP/DOWN    # in #pods

Initialization;
while system is running do:
	for each CDT do 
		resource_limit=get_resource_limit()
		resource_utilization=get_resource_utilization()
		max_workload_per_pod=(resource_limit*current_workload)/resource_utilization
		predicted_future_pods=predicted_workload/max_workload_per_pod
		current_pods=get_replica_count()
		if predicted_future_pods > current_pods then:
			pods_t+1=predicted_future_pods
			SCALE_UP(pods_t+1) ;
		else if predicted_future_pods < current_pods then:
			pods_t=current_pods
  		 	pods_t+1=max(predicted_future_pods,pods_minimum)
			podssurplus = (pods_t − pods_t+1 ) * RRS ;
			pods_t+1 = pods_t − (podssurplus ) ;
			SCALE_DOWN(pods_t+1) ;
		else
			Do nothing ;
		end
	end
end

Resource get_resource_utilization(){
Avg_Resource1_usage,Avg_Resource2_usage...,Avg_ResourceN_usage
for each pod in workload resource(Deployment or StatefulSet) do
	for each container in pod do
		Resource1_usage=get_resource_utilization(Resource1)
		Resource2_usage=get_resource_utilization(Resource2)
		.
		.
		ResourceN_usage=get_resource_utilization(ResourceN)
		Avg_Resource1_usage=Avg_Resource1_usage+Resource1_usage
		Avg_Resource2_usage=Avg_Resource2_usage+Resource2_usage
		.
		.
		Avg_ResourceN_usage=Avg_ResourceN_usage+ResourceN_usage

Avg_Resource1_usage=Avg_Resource1_usage/N
Avg_Resource2_usage=Avg_Resource2_usage/N
.
.
Avg_ResourceN_usage=Avg_ResourceN_usage/N		
		
Resource=get_Resource_utilization_of_bottelneck_resource(Avg_Resource1_usage,Avg_Resource2_usage...,Avg_ResourceN_usage)	
return Resource
} 

Resource get_resource_limit(){
  Resource=get_Resource_limits_of_bottelneck_resource(Avg_Resource1_usage,Avg_Resource2_usage...,Avg_ResourceN_usage)	
  return  
}
