def successful_offense(df,team='HOME'):

    #1. Understand if you want HOME or AWAY Team
    if team=='HOME':
        select_team = 0
    else:
        select_team = 1

        
    ### 2. Each Game has HOME and AWAY Teams. We're going to combine
    ### 2.1 Create a df_home. We're Dropping the AWAY information, and renaming columns
    df_home = df.loc[(df['AwayPlay'].isna())]
    df_home = df_home.drop(['AwayTeam', 'AwayPlay','AwayScore'],axis=1)
    df_home.rename(columns={'HomeTeam':'Team',
                            'HomePlay':'Play',
                            'HomeScore':'Score'}, inplace=True)


    ### 2.2 Create a df_away. We're Dropping the AWAY information, and renaming columns
    df_away = df.loc[(df['HomePlay'].isna())]
    df_away = df_away.drop(['HomeTeam', 'HomePlay','HomeScore'],axis=1)
    df_away.rename(columns={'AwayTeam':'Team',
                            'AwayPlay':'Play',
                            'AwayScore':'Score'}, inplace=True)

    ### 2.3 Concatenate and new fields
    df = pd.concat([df_home, df_away])

    ### 3. Selecting only the relevant information

    ### 3.1 Selecting data of that has MAKES or MISS in the Play Column.
    searchfor = [' makes ', ' misses ']
    s = df['Play'].str.contains('|'.join(searchfor))
    df = df.loc[s]

    ### 3.2 Selecting only the fields we will be using
    df = df[['Team','Play','Shooter','ShotType','ShotOutcome','ShotDist','Assister']].reset_index(drop=True)
    
    
    ### 4. We need to enhance and fill the null data.

    ### 4.1 Create Shooter and Assister [Name and ID] Columns
    x = df.Shooter.str.split()
    df['ShooterName'] = x.str[:2].str.join(' ')
    df['ShooterID'] = x.str[3:].str.join(' ')

    y = df.Assister.str.split()
    df['AssisterName'] = y.str[:2].str.join(' ')
    df['AssisterID'] = y.str[3:].str.join(' ')

    ### 4.2 Enhance Freethrow Data

    ### 4.2.1 Create The ShotType 'Free Throw'
    freethrow = df.iloc[:,1].str.contains('free throw')
    df.loc[freethrow, 'ShotType'] = 'free throw'

    ### 4.2.2 Create The Shooter Name from 'Free Throw'
    s = df.iloc[:,1].str.split()
    freethrowName = s.str[:2].str.join(' ')
    df['freethrowName'] = freethrowName
    df['ShooterName'] = df['ShooterName'].fillna(df.pop('freethrowName'))


    ###  4.2.3 Create Free Throw make or miss
    makes_ = df['Play'].str.contains(' makes ')
    misses_ = df['Play'].str.contains(' misses ')
    df.loc[makes_, 'ShotOutcome'] = 'make'
    df.loc[misses_, 'ShotOutcome'] = 'miss'

    ### 4.2.4 Distance of a freethrow (15 feet) https://official.nba.com/rule-no-1-court-dimensions-equipment/
    df['ShotDist'] = df['ShotDist'].fillna(15)

    ### 5. Create ShotValue
    df['ShotValue'] = 0
    df.loc[(df['ShotOutcome']=='make')&(df['ShotType'].str.contains('free throw')), 'ShotValue'] = 1
    df.loc[(df['ShotOutcome']=='make')&(df['ShotType'].str.contains('2-pt')), 'ShotValue'] = 2
    df.loc[(df['ShotOutcome']=='make')&(df['ShotType'].str.contains('3-pt')), 'ShotValue'] = 3

    ### 6. All AssisterName that are null, we will substituting it for ShooterName
    df.AssisterName.fillna(df.ShooterName, inplace=True)

    ### 7. Prepare the Dataset that we need moving forward
    df = df.loc[(df['ShotOutcome']=='make')] [['Team','ShooterName','ShotValue','ShotDist','ShotType','AssisterName','ShotOutcome']]

    ### 8. We're selecting only ONE Team
    team_selected = str(list(df['Team'].unique())[select_team])
    df = df.loc[(df['Team']==team_selected)].reset_index(drop=True)
    
    return df
    
