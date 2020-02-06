# A3-Streaming-Messaging-with-Apache-KafkaAufgabe


1.) Read Kafka Messaging and the links to the Kafka Libraries (e.g. in Python) to get ready for the next exercise.

Programm (!) two Kafka Producers writing to the same topic (using Java, Python, etc.)

Producer A writes even numbers every second, the other Producer B writes off numbers every two seconds to the topic.

Your consumer C reads the numbers and prints them with the origin A or B.

In practice: You start the e.g. three Python Scripts independently (not implementing the fork / concurrency etc. by hand)! (First you strt the zookeper and the Kafka server)

# Kafka Streams
Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in Kafka clusters. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka's server-side cluster technology
