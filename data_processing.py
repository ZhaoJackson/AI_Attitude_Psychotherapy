"""
Data utilities for SDT-AI Acceptance Analysis
Contains functions for loading and processing data
"""
import pandas as pd
import numpy as np

def create_composite_scores_cn(df):
    """
    Create composite scores for Chinese dataset
    """
    df_clean = df.copy()
    
    # TENS_Life (SDT): TENS_Life_1r through TENS_Life_9
    tens_cols = [f'TENS_Life_{i}r' if i <= 6 else f'TENS_Life_{i}' 
                 for i in range(1, 10)]
    tens_cols = [col for col in tens_cols if col in df_clean.columns]
    if tens_cols:
        df_clean['TENS_Life_mean'] = df_clean[tens_cols].mean(axis=1, skipna=True)
        print(f"TENS_Life_mean created from {len(tens_cols)} items")
    
    # GAAIS (General AI Attitudes): Already computed or need to compute from items
    if 'GAAIS_pos' in df_clean.columns and 'GAAIS_neg' in df_clean.columns:
        # If already computed, use them
        df_clean['GAAIS_mean'] = (df_clean['GAAIS_pos'] - df_clean['GAAIS_neg'].replace({np.nan: 0}) + 7) / 2
    else:
        # Compute from individual items (GAAIS_1 to GAAIS_10)
        gaais_pos_cols = [f'GAAIS_{i}' for i in range(1, 6) if f'GAAIS_{i}' in df_clean.columns]
        gaais_neg_cols = [f'GAAIS_{i}' for i in range(6, 11) if f'GAAIS_{i}' in df_clean.columns]
        if gaais_pos_cols and gaais_neg_cols:
            pos_mean = df_clean[gaais_pos_cols].mean(axis=1, skipna=True)
            neg_mean = df_clean[gaais_neg_cols].mean(axis=1, skipna=True)
            # Reverse score negative items and create overall mean
            df_clean['GAAIS_mean'] = (pos_mean + (8 - neg_mean)) / 2
    
    # Epistemic Trust: ET_1 through ET_15
    et_cols = [f'ET_{i}' for i in range(1, 16) if f'ET_{i}' in df_clean.columns]
    if et_cols:
        df_clean['ET_mean'] = df_clean[et_cols].mean(axis=1, skipna=True)
        print(f"ET_mean created from {len(et_cols)} items")
    
    # Stigma: SSRPH_1 through SSRPH_5
    ssrph_cols = [f'SSRPH_{i}' for i in range(1, 6) if f'SSRPH_{i}' in df_clean.columns]
    if ssrph_cols:
        df_clean['SSRPH_mean'] = df_clean[ssrph_cols].mean(axis=1, skipna=True)
        print(f"SSRPH_mean created from {len(ssrph_cols)} items")
    
    # Depression: PHQ5_1 through PHQ5_5
    phq5_cols = [f'PHQ5_{i}' for i in range(1, 6) if f'PHQ5_{i}' in df_clean.columns]
    if phq5_cols:
        df_clean['PHQ5_mean'] = df_clean[phq5_cols].mean(axis=1, skipna=True)
        print(f"PHQ5_mean created from {len(phq5_cols)} items")
    
    # UTAUT_AI: Create overall mean
    utaut_ai_cols = [col for col in df_clean.columns if col.startswith('UTAUT_AI') and col.replace('UTAUT_AI', '').isdigit()]
    utaut_ai_cols_r = [col for col in df_clean.columns if col.startswith('UTAUT_AI') and 'r' in col]
    
    # Handle reverse-coded items
    if utaut_ai_cols:
        for col in utaut_ai_cols_r:
            if col in df_clean.columns:
                df_clean[col] = 8 - df_clean[col]
        
        all_utaut_ai = [col for col in utaut_ai_cols + utaut_ai_cols_r if col in df_clean.columns]
        if all_utaut_ai:
            df_clean['UTAUT_AI_mean'] = df_clean[all_utaut_ai].mean(axis=1, skipna=True)
            print(f"UTAUT_AI_mean created from {len(all_utaut_ai)} items")
    
    # Behavioral Intention: would_you_use_1 through would_you_use_7
    wyu_cols = [f'would_you_use_{i}' for i in range(1, 8) if f'would_you_use_{i}' in df_clean.columns]
    if wyu_cols:
        df_clean['would_you_use_mean'] = df_clean[wyu_cols].mean(axis=1, skipna=True)
        print(f"would_you_use_mean created from {len(wyu_cols)} items")
    
    # Role: Create binary role variable (1=therapist, 0=client)
    if 'therapist' in df_clean.columns:
        df_clean['role'] = df_clean['therapist'].map({1.0: 1, 0.0: 0})
    else:
        df_clean['role'] = 0
    
    # Country identifier
    df_clean['country'] = 'China'
    
    return df_clean

def create_composite_scores_usa(df):
    """
    Create composite scores for USA dataset
    """
    df_clean = df.copy()
    
    # TENS_Life: TENS_Life_1 through TENS_Life_9
    tens_cols = [f'TENS_Life_{i}' for i in range(1, 10) if f'TENS_Life_{i}' in df_clean.columns]
    if tens_cols:
        # Reverse score items 1-6
        for i in range(1, 7):
            col = f'TENS_Life_{i}'
            if col in df_clean.columns:
                df_clean[col] = 8 - df_clean[col]
        df_clean['TENS_Life_mean'] = df_clean[tens_cols].mean(axis=1, skipna=True)
        print(f"TENS_Life_mean created from {len(tens_cols)} items")
    
    # GAAIS
    if 'GAAIS_pos' in df_clean.columns and 'GAAIS_neg' in df_clean.columns:
        df_clean['GAAIS_mean'] = (df_clean['GAAIS_pos'] - df_clean['GAAIS_neg'].replace({np.nan: 0}) + 7) / 2
    else:
        gaais_cols = [f'GAAIS_{i}' for i in range(1, 11) if f'GAAIS_{i}' in df_clean.columns]
        if gaais_cols:
            pos_cols = gaais_cols[:5]
            neg_cols = gaais_cols[5:]
            if pos_cols and neg_cols:
                pos_mean = df_clean[pos_cols].mean(axis=1, skipna=True)
                neg_mean = df_clean[neg_cols].mean(axis=1, skipna=True)
                df_clean['GAAIS_mean'] = (pos_mean + (8 - neg_mean)) / 2
    
    # Epistemic Trust
    et_cols = [f'ET_{i}' for i in range(1, 16) if f'ET_{i}' in df_clean.columns]
    if et_cols:
        df_clean['ET_mean'] = df_clean[et_cols].mean(axis=1, skipna=True)
        print(f"ET_mean created from {len(et_cols)} items")
    
    # Stigma
    ssrph_cols = [f'SSRPH_{i}' for i in range(1, 6) if f'SSRPH_{i}' in df_clean.columns]
    if ssrph_cols:
        df_clean['SSRPH_mean'] = df_clean[ssrph_cols].mean(axis=1, skipna=True)
        print(f"SSRPH_mean created from {len(ssrph_cols)} items")
    
    # Depression
    phq5_cols = [f'PHQ_5_{i}' for i in range(1, 6) if f'PHQ_5_{i}' in df_clean.columns]
    if phq5_cols:
        df_clean['PHQ5_mean'] = df_clean[phq5_cols].mean(axis=1, skipna=True)
        print(f"PHQ5_mean created from {len(phq5_cols)} items")
    
    # UTAUT_AI: Use UTAUT_AIavatar columns
    utaut_ai_cols = [col for col in df_clean.columns if col.startswith('UTAUT_AIavatar_') and not col.endswith('r')]
    utaut_ai_cols_r = [col for col in df_clean.columns if col.startswith('UTAUTr_AIavatar_')]
    
    for col in utaut_ai_cols_r:
        if col in df_clean.columns:
            df_clean[col] = 8 - df_clean[col]
    
    all_utaut_ai = [col for col in utaut_ai_cols + utaut_ai_cols_r if col in df_clean.columns]
    if all_utaut_ai:
        df_clean['UTAUT_AI_mean'] = df_clean[all_utaut_ai].mean(axis=1, skipna=True)
        print(f"UTAUT_AI_mean created from {len(all_utaut_ai)} items")
    
    # Behavioral Intention
    wyu_cols = [f'would_you_use_{i}' for i in range(1, 8) if f'would_you_use_{i}' in df_clean.columns]
    if wyu_cols:
        df_clean['would_you_use_mean'] = df_clean[wyu_cols].mean(axis=1, skipna=True)
        print(f"would_you_use_mean created from {len(wyu_cols)} items")
    
    # Role
    if 'Therapist_or_mental_' in df_clean.columns:
        df_clean['role'] = df_clean['Therapist_or_mental_'].map({1.0: 1, 2.0: 0, 3.0: 0})
    elif 'therapistORcommunity' in df_clean.columns:
        df_clean['role'] = df_clean['therapistORcommunity'].map({'therapist': 1, 'client': 0, 'community': 0})
    else:
        df_clean['role'] = 0
    
    # Country identifier
    df_clean['country'] = 'USA'
    
    # Age and Gender harmonization
    if 'Age' in df_clean.columns:
        df_clean['age'] = df_clean['Age']
    if 'Gender' in df_clean.columns:
        df_clean['gender'] = df_clean['Gender']
    
    return df_clean

def load_and_prepare_data():
    """
    Load and prepare combined dataset for analysis
    Returns combined_data DataFrame
    """
    # Load data
    cn_all = pd.read_csv('data/china/CN_all.csv')
    usa_all = pd.read_csv('data/usa/USA_all.csv')
    
    # Create composite scores
    cn_all = create_composite_scores_cn(cn_all)
    usa_all = create_composite_scores_usa(usa_all)
    
    # Select key variables
    key_vars = ['TENS_Life_mean', 'UTAUT_AI_mean', 'GAAIS_mean', 'ET_mean', 
                'SSRPH_mean', 'PHQ5_mean', 'would_you_use_mean', 
                'age', 'gender', 'role', 'country']
    
    # Create combined dataset
    cn_analysis = cn_all[key_vars + ['ID'] if 'ID' in cn_all.columns else key_vars].copy()
    
    usa_analysis = usa_all[key_vars + ['ResponseId'] if 'ResponseId' in usa_all.columns else key_vars].copy()
    if 'ResponseId' in usa_all.columns:
        usa_analysis = usa_analysis.rename(columns={'ResponseId': 'ID'})
    
    # Combine datasets
    combined_data = pd.concat([cn_analysis, usa_analysis], ignore_index=True)
    
    # Create country code
    combined_data['country_code'] = combined_data['country'].map({'USA': 0, 'China': 1})
    
    # Remove rows with missing key variables
    combined_data = combined_data.dropna(subset=['TENS_Life_mean', 'UTAUT_AI_mean'])
    
    return combined_data

