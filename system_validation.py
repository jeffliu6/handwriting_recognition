import preprocessor as pre
import classifier
import postprocessor as post
import constants as c
import sys
import os

if __name__ == "__main__":
    print("Beginning system testing protocol...")
    if os.path.isdir(c.PATH_TO_VDATA):
        files = [f for f in os.listdir(c.PATH_TO_VDATA)]
        files.sort()
        with open(c.PATH_TO_VDATA + files[1]) as f:
            expected_data = f.read().splitlines()
        success = []
        failure = []
        assert(len(files[2:]) == len(expected_data))
        for idx,vd_img in enumerate(files[2:]):
            expected = expected_data[idx].split(",")
            str_rep = classifier.classify(pre.process_image(c.PATH_TO_VDATA+vd_img))
            result = post.postProcess(str_rep)
            if isinstance(result, Exception):
                failure.append((vd_img,result))
            elif result[0] == expected[0] and result[1] == expected[1]:
                success.append(vd_img)
            else:
                failure.append((vd_img,"Expected: "+str(expected)+" but got " +str(result)))
        if(len(success) == 0):
            succ_rate = "0.0"
        else:
            succ_rate = str(float(float(len(success))/(float(len(failure)) + float(len(success)))))
        print("Success rate: "+ succ_rate)
        print("The following validation images failed: ")
        for f in failure:
            print(f[0]+": "+str(f[1]))

else:
    print("Bad path to validation data")

