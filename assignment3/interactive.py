# tarot card dataset : https://github.com/metabismuth/tarot-json/releases/tag/v0
import json
import cv2
import numpy as np
import asyncio
import textwrap

# map for lifepath sums that are a single digit
digit_map = {
    1: 10,
    2: 11,
    3: 12,
    4: 13,
    5: 14,
    6: 15,
    7: 16,
    8: 17,
    9: 18
}

# load data from json with possible results
with open('tarot_results.json', 'r') as f:
    data = json.load(f)

# calculate lifepath number based on birthdate
def calculateLifePath(birthDate):
    #split birthday by two digits and add
    month = int(birthDate[0]) + int(birthDate[1])
    day = int(birthDate[2]) + int(birthDate[3])
    year1 = int(birthDate[4]) + int(birthDate[5])
    year2 = int(birthDate[6]) + int(birthDate[7])

    sum1 = month + day + year1 + year2

    #reduce first sum to a 2 digit number if 3 digits
    sum2 = None
    if len(str(sum1)) == 3:
        sum2 = int(str(sum1)[0:2]) + int(str(sum1)[-1])
    elif len(str(sum1)) == 2:
        #if 2 digits, reduce if over 21 (major arcana only go up to 21)
        if not sum1 <= 21:
            sum2 = int(str(sum1)[0]) + int(str(sum1)[1])
        else:
            sum2 = sum1    
    else:
        # if single digit, do nothing
        sum2 = sum1

    # second sum reduction
    sum3 = None
    if len(str(sum2)) == 2:
        if not sum2 <= 21:
            sum3 = int(str(sum2)[0]) + int(str(sum2)[1])
        else:
            sum3 = sum2
    else:
        sum3 = sum2

    # redirect single digit sums to corresponding birth card pair
    if len(str(sum3)) == 1:
        final_sum = digit_map[sum3]
    else:
        final_sum = sum3

    return final_sum

async def showResult(lifePath):
    # get result data
    result = data[str(lifePath)]
    
    #get filepath to card images
    card_images = []
    for num in range(len(result["card_num"])):
        filepath = "deck_images/m" + result["card_num"][num] + ".jpg"
        print(filepath)
        card_images.append(cv2.imread(filepath))

    #isplay result
    # get result information to display
    result_title = result["card_pair"]
    result_msg = textwrap.wrap(result["message"], width=35) #wrap message to fit in window

    # create result display window
    window_width = 2000
    window_height = 1000
    label_height = round(window_height/8)*2
    width_margin = round(window_width/24)
    output_display = np.ones((window_height,window_width,3), np.uint8)*225

    # add result title to display window
    cv2.putText(output_display, result_title, 
                (64, 148), cv2.FONT_HERSHEY_SIMPLEX, 2, (42, 42, 165), 3,cv2.LINE_AA, bottomLeftOrigin=False)
    
    # display first card
    card1 = {
        "x1": width_margin,
        "x2": card_images[0].shape[1]+width_margin
    }
    output_display[label_height:card_images[0].shape[0]+label_height, card1["x1"]:card1["x2"]] = card_images[0]

    # display second card
    card2 = {
        "x1": card1["x2"] + 24,
        "x2": card1["x2"] + 24 + card_images[1].shape[1]
    }
    output_display[label_height:card_images[1].shape[0]+label_height, card2["x1"]:card2["x2"]] = card_images[1]

    #display third card, if any
    if len(card_images) == 3:
        card3 = {
            "x1": card2["x2"] + 24,
            "x2": card2["x2"] + 24 + card_images[2].shape[1]
        }
        output_display[label_height:card_images[2].shape[0]+label_height, card3["x1"]:card3["x2"]] = card_images[2]

        #add message text, wrappedtext is not string so modify display window np array
        for i, line in enumerate(result_msg):
            textsize = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]

            gap = textsize[1] + 14

            y = int((label_height + textsize[1])) + i * gap
            x = int(((output_display.shape[1]-width_margin) - textsize[0]))

            cv2.putText(output_display, line, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        1, 
                        (42, 42, 165), 
                        2, 
                        lineType = cv2.LINE_AA)
    else:
        #add message text, wrappedtext is not string so modify display window np array
        for i, line in enumerate(result_msg):
            textsize = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]

            gap = textsize[1] + 14

            y = int((label_height + textsize[1])) + i * gap
            x = int(((output_display.shape[1]-width_margin) - textsize[0]))

            cv2.putText(output_display, line, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                        1, 
                        (42, 42, 165), 
                        2, 
                        lineType = cv2.LINE_AA)

    
    
    # show result in a separate window
    while True:
        cv2.imshow("Result", output_display)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

async def main():
    while True:
        print('Please input your birthday in the form MMDDYY. For example: January 2nd, 1999 would be 01021999')
        birthDate = input()

        # ensure that input is the correct length
        if not len(birthDate) == 8:
            print('Incorrect format inputted, please try again.')
            continue

        #check that the input is correct format
        try:
            int(birthDate)
        except:
            print('Incorrect format inputted, please try again.')
            continue

        # calculate and show result
        lifePath = calculateLifePath(birthDate)
        await showResult(lifePath)

        # after first result is quit, ask user if they want to try again
        restart = input('Ask another birthday? y/n \n')
        if restart.lower() == 'y':
            continue
        else:
            break

if __name__ == '__main__':
    #run program
    asyncio.run(main())


#TODO: add keyword inputs such as favorite animal to customize a tarot card?