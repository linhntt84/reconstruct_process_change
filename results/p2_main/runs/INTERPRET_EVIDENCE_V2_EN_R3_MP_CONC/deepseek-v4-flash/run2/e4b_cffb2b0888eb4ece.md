### Observed differences

- In the later window, activity A16 is performed by a single resource (User_8) in all observed cases, whereas earlier it was spread across 17 resources with the most frequent taking about 18% of cases. [ASSIGN001, CONC001]
- The elapsed time between activities A09 and A23 increased from a median of about 1.3 hours to about 16.1 hours; the mean rose from about 2.2 to 15.6 hours. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in resource allocation for activity A16: in the later window, A16 is consistently assigned to one resource (User_8), while earlier it was distributed among many resources. This is directly shown by the assignment distribution and the concentration index, both based on about 150 traces per window. [ASSIGN001, CONC001]

Other differences: The time between A09 and A23 increased substantially, suggesting a timing change, though it is based on fewer observations (22 and 26 traces). [TWAIT001]

A competing explanation for the timing difference is that the sample of traces containing both activities is small, but the magnitude and consistency of the increase make it unlikely to be random.