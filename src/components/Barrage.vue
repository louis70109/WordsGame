<template>
  <div class="barrage">
    <button type="button" @click="startRandomPushWords()">開始</button>
    <button type="button" @click="clearRandomPushWords()">結束</button>
    <h3>秒數：{{ timeCount }}</h3>
    <input
      id="answer_input"
      type="text"
      v-model="answer"
      @keyup.enter="findBullet()"
    />
  </div>
</template>

<script>
import { ref } from 'vue';
import gsap from 'gsap';
import { createGame, setStyle } from '../utils/users';
export default {
  setup() {
    let data = ref([]),
      answer = '',
      count = ref(0),
      intervalControl = null,
      timeCount = ref(30),
      userRecord = ref(0),
      basicSetting = setStyle();
    const words = {
      a: ['あ'],
      ka: ['か'],
      sa: ['さ'],
      ta: ['た'],
      na: ['な'],
      ha: ['は'],
      ma: ['ま'],
      ya: ['や'],
      ra: ['ら'],
      wa: ['わ'],
      i: ['い'],
      ki: ['き'],
      shi: ['し'],
      chi: ['ち'],
      ni: ['に'],
      hi: ['ひ'],
      mi: ['み'],
      ri: ['り'],
      u: ['う'],
      ku: ['く'],
      su: ['す'],
      tsu: ['つ'],
      nu: ['ぬ'],
      fu: ['ふ'],
      mu: ['む'],
      yu: ['ゆ'],
      ru: ['る'],
      n: ['ん'],
      e: ['え'],
      ke: ['け'],
      se: ['せ'],
      te: ['て'],
      ne: ['ね'],
      he: ['へ'],
      me: ['め'],
      re: ['れ'],
      o: ['お'],
      ko: ['こ'],
      so: ['そ'],
      to: ['と'],
      no: ['の'],
      ho: ['ほ'],
      mo: ['も'],
      yo: ['よ'],
      ro: ['ろ'],
      wo: ['を'],
    };

    function startRandomPushWords() {
      intervalControl = setInterval(() => {
        console.log('Random push words start');
        let randomIndex = Math.floor(Math.random() * Object.keys(words).length);
        const publishWord = Object.keys(words)[randomIndex - 1];
        console.log(publishWord);
        let randomWordIndex = Math.floor(
          Math.random() * Object.keys(words[publishWord]).length
        );
        console.log(words[publishWord][randomWordIndex]);
        createText(words[publishWord][randomWordIndex]);
        timeCount.value -= 1; // temp timer

        // Time out
        if (timeCount.value === 0) {
          timeCount.value = 0;
          clearRandomPushWords();
          alert(`時間到！！！ 分數為： ${userRecord.value}`);
        }
      }, 1000);
    }
    function clearRandomPushWords() {
      clearInterval(intervalControl);
      createGame({score: userRecord.value, level: basicSetting.level});
      cleanBullet();
      console.log('interval stop');
    }

    function findBullet() {
      let bullets = bulletFormat();

      if (this.answer in words && Object.keys(bullets).length !== 0) {
        console.log('答對');
        for (let key in bullets) {
          if (words[this.answer].indexOf(bullets[key]) !== -1) {
            document.getElementById(key).remove();
            removeBulletFromStorage(bullets[key], key);
            userRecord.value += 1;
            break;
          }
        }
      } else console.log('答錯 or 空的');
      this.answer = '';
      document.getElementById('answer_input').value = '';
    }

    function bulletFormat() {
      let bullets = localStorage.getItem('bullets');
      // list of dict
      // {
      //   'あ': 'class-1',
      // }
      if (bullets) return JSON.parse(bullets);
      return {};
    }

    function cleanBullet() {
      localStorage.setItem('bullets', '{}');
    }

    function removeBulletFromStorage(text, tagId) {
      let bullets = bulletFormat(),
        wordCondition = false;
      for (let i in words) {
        if (words[i].indexOf(text) !== -1) {
          wordCondition = true;
          break;
        }
      }
      if (wordCondition && tagId in bullets) {
        delete bullets[tagId];
        localStorage.setItem('bullets', JSON.stringify(bullets));
      }
    }

    function addBulletToStorage(text, tagId) {
      let bullets = bulletFormat();
      bullets[tagId] = text;
      // text -> 'あ'
      // {
      //   'class-1': 'あ',
      // }

      localStorage.setItem('bullets', JSON.stringify(bullets));
    }
    function setBulletBody() {
      let div_text = document.createElement('div');
      div_text.id = 'text' + (count.value += 1);
      div_text.style.position = 'fixed';
      div_text.style.whiteSpace = 'nowrap';

      div_text.style.left = document.documentElement.clientWidth + 'px';
      const random = Math.round(
        Math.random() * document.documentElement.clientHeight
      );

      div_text.style.top = random + 'px';
      div_text.style.color = basicSetting.color
      div_text.style.fontSize = basicSetting.size
      return div_text
    }
    async function createText(text) {
      let div_text = setBulletBody()

      if (text) {
        div_text.appendChild(document.createTextNode(text));
        document.body.appendChild(div_text);
        addBulletToStorage(text, div_text.id);
      }
      await gsap.to('#' + div_text.id, {
        duration: basicSetting.duration,
        x: -1 * (document.documentElement.clientWidth + div_text.clientWidth),
      });
      if (div_text.hasChildNodes()) {
        div_text.parentNode.removeChild(div_text); // TODO: judge the local storage items
        removeBulletFromStorage(text, div_text.id);
      }
    }
    return {
      count,
      answer,
      words,
      data,
      timeCount,
      userRecord,
      createText,
      findBullet,
      startRandomPushWords,
      clearRandomPushWords,
    };
  },
};
</script>
