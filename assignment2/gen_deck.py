# messages are taken from: https://labyrinthos.co/blogs/learn-tarot-with-labyrinthos-academy/how-to-calculate-your-tarot-birth-card-plus-short-birth-card-meanings-infographic?srsltid=AfmBOorHPTalNfpdN2_On6USAQoHp0Uumn_mbd7rufxllXn8IXA-FU65

import json

birth_card_map = {
    10: "Wheel of Fortune/Magician",
    11: "Justice/High Priestess",
    12: "Hanged Man/Empress",
    13: "Death/Emperor",
    14: "Temperance/Hierophant",
    15: "Devil/Lovers",
    16: "Tower/Chariot",
    17: "Star/Strength",
    18: "Moon/Hermit",
    19: "Sun/Wheel of Fortune/Magician",
    20: "Judgement/High Priestess",
    21: "World/Empress"
}

msg_map = {
    10: "These birth cards deal with following the cyclic change of the universe and the random hand of fate (The Wheel of Fortune) using the manifestation powers and resourcefulness of the Magician. Wherever the wheel shifts, you will be ready.",
    11: "Your path unites clarity, fairness and harmony with deep intuitive understanding and knowledge. Justice and the High Priestess are concerned with two different sides in life - the transactional and the spiritual. Your insights tend to go deeply, a powerful compliment with Justice’s objectivity and sharp decision making.",
    12: "This path represents gentle progress during moments of delays, and the willful sacrifices of the Hanged Man made with the nurturing care of the Empress. When faced with the Hanged Man’s deliberate choice to remain in his suspension, the love within the empress guides him to continue his spiritual path.",
    13: "In this path, the Death card represents the ending of cycles - of closing doors to open others anew. It is here where the Emperor’s power, authority and structure are needed in order to create stability and security. For the new cycle to be ushered in, a strong and willful hand will be needed to steer its movement.",
    14: "Your path is one of guidance - of using your great wisdom (The Hierophant) to bring calm and peace to conflict (Temperance). Having these two cards come together is akin to having two great advisors - one bearing the keys to long established knowledge, and the other equipped with the gentle serenity to unify disparate groups.",
    15: "Deep sensuality is indicated by this birth card pair - for the Devil is the combination of both the divine and the beastly. He is playful in the realm of the material, but his pure enjoyment can lead some to be enslaved. The lovers however bring an element of love to his passionate animalistic nature. His beauty in the horror is redeemed.",
    16: "Yours is the path of restoring balance in the face of violent transformation. In the face of groundbreaking change, it is your sense of balance that will be your guide. The Tower destroys foundations and structure ruthlessly in order to reveal a new path forward, but this energy will be guided by the Chariot’s deliberate and careful control of impulses.",
    17: "This path is one of hope - of the choice to look at all that life brings you with optimism (The Star), requiring of you great inner Strength. Yours is the choice of moving away from sorrow, towards regeneration, which takes great resilience in times of suffering. To have hope is the source of your action, to have Strength is assurance that you will succeed.",
    18: "Your path is about finding the clarity in the darkness, about finding truth in an uncertain world. The Moon presents us with phantoms, dreams and illusions. It is about the hidden facets that are just below the surface. The hermit is the seeker, who uses their internal truth to light the way to finding your own personal wisdom.",
    19: "Like the Wheel and Magician birth cards, this path is about adapting to change, and moving alongside nature’s cycles resourcefully. It is about recognizing and understanding the natural shifts of the universe (The Wheel of Fortune) while using your inner powers of manifestation and creation to move along with those cycles with grace and success (The Magician). The Sun gives an air of contentment, joy and peace to this path, giving you the cue to enjoy the abundance that your path brings you.",
    20: "This path is one of breaking limitations, of releasing oneself from established modes of thought, and rebuilding them anew (Judgement). You will be guided by your intuition (The High Priestess), and it is through learning to trust your inner voice that you will create your most important work.",
    21: "Your path is one of self-actualization, to bring together all the disparate parts of yourself in order to feel completely at home in this world (The World). Throughout this path, you will be guided by love - both giving and receiving love (The Empress). This loving and caring aspect within you will be your compass towards fulfillment, and is the gift you give to all others."
}

birth_num_map = {}
for i in range(10,22):
    added_nums = []
    added_nums.append(str(i))
    #add down the two digits into one
    single = int(str(i)[0]) + int(str(i)[1])
    added_nums.append("0" + str(single))
    if i == 19:
        #19 will add down once more
        added_nums.append("01")

    #add final result to map
    birth_num_map[i] = added_nums

result = {}
for i in range(10, 22):
    result[i] = {
        "card_pair":birth_card_map[i],
        "card_num": birth_num_map[i],
        "message": msg_map[i]
    }

output_path = "tarot_results.json"
with open(output_path, 'w') as f:
    data = json.dumps(result)
    f.write(data)

f.close()