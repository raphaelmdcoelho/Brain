A file system defines how files are named, stored, and retrieved from a storage device.

Every time you open a file on your computer or smart device, your operating system uses its file system internally to load it from the storage device. Or when you copy, edit, or delete a file, the file system handles it under the hood.

When people talk about file systems, they might refer to different aspects of a file system depending on the context - that's where things start to seem knotty.

The term file system takes its name from the old paper-based data management systems, where we kept documents as files and put them into directories.

Space management, metadata, data encryption, ==file access control==, and data integrity are the responsibilities of the file system too.

==Storage devices must be  **partitioned**  and  **formatted**  before the first use==.

[[Partitioning]] is splitting a storage device into several  _logical regions_, so they can be managed separately as if they are separate storage devices.

We usually do partitioning by a disk management tool provided by operating systems, or as a command-line tool provided by the system's firmware.

For example, a basic Linux installation has three partitions: one partition dedicated to the operating system, one for the users' files, and an optional swap partition.

A swap partition works as the RAM extension when RAM runs out of space.

#filesystem #computing 
