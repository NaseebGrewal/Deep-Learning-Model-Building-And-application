from setuptools import setup, find_packages

setup(
    name='deep_learning_model_building_and_applicaton',  # Replace with your project name
    version='0.1.9',
    packages=find_packages(where='./DeepLearning.AI Short Courses/AI_Python_for_Beginner/'),  # Automatically find packages in your project
    package_dir={'': './DeepLearning.AI Short Courses/AI_Python_for_Beginner'},
    install_requires=[
        # List any dependencies your project needs, e.g.:
        # 'numpy',
    ],
    author='Learn Tech',
    description='Deep Learning for Beginners',
)
