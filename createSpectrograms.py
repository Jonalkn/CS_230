import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--audio_dir', default='data/wav_songs', help="Directory with the .wav SONGS dataset")
parser.add_argument('--output_dir', default='data/raw_specs', help="Where to write the new data")
pixpersec = 50

if __name__ == '__main__':
	args = parser.parse_args()

	audio_dir = args.audio_dir
	specs_dir = args.output_dir

	assert os.path.isdir(audio_dir), "Couldn't find the dataset at {}".format(audio_dir)

	if not os.path.exists(specs_dir):
		os.mkdir(specs_dir)
	else:
		print("Warning: output dir {} already exists".format(specs_dir))


	for fname in os.listdir(audio_dir):
		if fname.endswith(".wav"):
			source = os.path.join(audio_dir, fname)
			dest = os.path.join(specs_dir, str(fname.split(".")[0])+".png")
			command = ['sox', source, '-n', 'remix', '1','spectrogram', '-Y', '200', '-X', str(pixpersec), '-m', '-r', '-o', dest]
			subprocess.call(command)






