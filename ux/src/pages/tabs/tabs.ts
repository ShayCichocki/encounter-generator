import { Component } from "@angular/core";
import { CreatureSearchPage } from "../creature-search/creature-search";
import { EncounterPage } from "../encounter/encounter";
import { EncounterCreationPage } from "../encounter-creation/encounter-creation";

@Component({
    selector: 'page-tabs',
    template: `
    <ion-tabs>
        <ion-tab [root]="encounterPage" tabTitle="Encounter" tabIcon="star"></ion-tab>
        <ion-tab [root]="creatureSearchPage" tabTitle="Search" tabIcon="book"></ion-tab>
        <ion-tab [root]="encounterCreationPage" tabTitle="Create" tabIcon="happy"></ion-tab>
    </ion-tabs>
    
    `
})

export class TabsPage{
    encounterPage = EncounterPage;
    creatureSearchPage = CreatureSearchPage;
    encounterCreationPage = EncounterCreationPage;
}