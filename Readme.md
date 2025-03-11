### Title: Dynamic Scaling of Pods Using Artificial Intelligence in Kubernetes 

### Project Description:
Traditional Kubernetes deployments rely on reactive Autoscaling techniques, like the Horizontal Pod Autoscaler (HPA), to regulate the number of pods counts based solely on current workload metrics. However, these native scalability features introduce latency in pod creation and often result in inefficient resource utilization during sudden workload surges. In this work, we introduce a Dynamic Pod Autoscaler (DPA) that leverages a hybrid AI forecasting model combining Bidirectional networks, Long Short-Term Memory (Bi-LSTM) and Gated Recurrent Unit (Bi-GRU). By continuously monitoring application performance metrics via Prometheus and integrating real-time data from HAProxy, our approach proactively predicts future workload trends. This predictive capability enables the system to preemptively adjust pod counts—scaling up to handle anticipated peaks and rapidly scaling down when demand subsides—thus offering superior responsiveness and cost efficiency compared to traditional reactive scaling. Experimental evaluations, including a real-world test on a high-traffic college website, demonstrate that our method not only reduces scaling latency and resource over-provisioning but also achieves optimal performance using fewer pods than the standard HPA. Consequently, our AI-driven dynamic scaling solution provides a robust, scalable, and efficient alternative to Kubernetes’ internal autoscaling mechanisms, paving the way for more resilient and resource-optimized cloud-native applications.


### The project is organized as follows
```
DPA
├── loadtest
├── manifests
│   ├── application
│   ├── HaProxy
│   ├── HPA
│   ├── kind.yaml
│   └── monitoring
├── Readme.md
├── results
├── sample_app
└── src
    ├── best_saved_model
    ├── core_algo
    ├── Dockerfile
    ├── models
    └── results
```
## loadtest
directory contains the locust loadtest library used to test on the sample application
## sample_app
directory is the sample node.js sever app deployed to test the DPA where the load is sent by locust
## results
contains the images of the research proceedings done on the DPA
## src
contains the core folder for the AI models and the DPA algorithm
```
    1.best_saved_model is the best model saved
    2.core_algo contains the DPA pseudo algorithm
    3.Docker file of the AI model
    4.models contains the AI models and the custom DPA controller code
    5.results contain the HPA vs DPA results
```

# For colloboration and improvements contact:
cheithanya2002@gmail.com