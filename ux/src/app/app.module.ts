import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { TabsPage } from '../pages/tabs/tabs';
import { CreatureSearchPage } from '../pages/creature-search/creature-search';
import { EncounterCreationPage } from '../pages/encounter-creation/encounter-creation';
import { EncounterPage } from '../pages/encounter/encounter';
import { DataFinder } from '../providers/datafinder';
import { HttpModule } from '@angular/http';
import { CreaturePage } from '../pages/creature/creature';
import { monsterService } from '../providers/monsterService';

@NgModule({
  declarations: [
    MyApp,
    TabsPage,
    CreatureSearchPage,
    EncounterCreationPage,
    EncounterPage,
    CreaturePage
  ],
  imports: [
    BrowserModule,
    HttpModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    TabsPage,
    CreatureSearchPage,
    EncounterCreationPage,
    EncounterPage,
    CreaturePage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    DataFinder,
    monsterService,
    
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
