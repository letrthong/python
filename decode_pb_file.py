# https://copilot.cloud.microsoft/
import tensorflow as tf

def load_pb_model(pb_file_path):
    # Load the protobuf file from the disk and parse it to retrieve the graph definition
    with tf.io.gfile.GFile(pb_file_path, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())

    # Import the graph definition into a new graph
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def, name="")

    return graph

# Example usage
pb_file_path = "20241220_045112.pb"
graph = load_pb_model(pb_file_path)

# To inspect the operations in the graph
for op in graph.get_operations():
    print(op.name)
