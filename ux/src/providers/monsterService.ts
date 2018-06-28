export class monsterService {
    private monsterList = []

    addMonsterToList(monster){
        this.monsterList.push(monster)
        console.log(this.monsterList);
    }

    getMonsterList(){
        return this.monsterList.slice();
    }

    totalCR(){
        var multiplier = [1,1,1.5,2,2,2,2,2.5,2.5,2.5,2.5,3,3,3,3,4];
        var CR = 0;
        for (let i = 0; i < this.monsterList.length; i++) {
            CR += this.monsterList[i].cr;
        }
        return Math.floor(CR * multiplier[this.monsterList.length -1]);
    }
}