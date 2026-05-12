import numpy as np
from PIL import Image

def nalozi_sliko(vhod):
    if isinstance(vhod, str):
        slika = Image.open(vhod).convert("L")
        arr = np.asarray(slika, dtype=np.float64)
    else:
        arr = np.array(vhod, dtype=np.float64)
    return arr

def normaliziraj_sliko(arr):
    if np.max(arr) <= 1.0:
        arr = arr * 256.0
    return arr

def ustvari_frekvencno_masko(vis, sir, prag):
    y, x = np.ogrid[:vis, :sir]
    center_y, center_x = vis // 2, sir // 2
    norm_y = (y - center_y) / vis
    norm_x = (x - center_x) / sir
    dist_sq = norm_x**2 + norm_y**2
    maska = (dist_sq >= prag**2).astype(float)
    return maska

def filtriraj_fft(arr, prag):
    vis, sir = arr.shape
    fft_slika = np.fft.fft2(arr)
    fft_center = np.fft.fftshift(fft_slika)

    maska = ustvari_frekvencno_masko(vis, sir, prag)
    fft_filtriran = fft_center * maska

    fft_nazaj = np.fft.ifftshift(fft_filtriran)
    slika_filtrirana = np.fft.ifft2(fft_nazaj).real
    slika_filtrirana = np.clip(slika_filtrirana, 0, 256)
    return slika_filtrirana

def izracunaj_MI(arr_org, arr_filt):
    st_bins = 256
    org_flat = arr_org.flatten()
    filt_flat = arr_filt.flatten()

    hist_org, _ = np.histogram(org_flat, bins=st_bins, range=(0, 256))
    hist_filt, _ = np.histogram(filt_flat, bins=st_bins, range=(0, 256))
    hist_joint, _, _ = np.histogram2d(org_flat, filt_flat, bins=st_bins, range=[[0, 256], [0, 256]])

    velikost = org_flat.size
    p_org = hist_org / velikost
    p_filt = hist_filt / velikost
    p_joint = hist_joint / velikost

    eps = 1e-12

    ent_org = -np.sum(p_org[p_org > 0] * np.log2(p_org[p_org > 0] + eps))
    ent_filt = -np.sum(p_filt[p_filt > 0] * np.log2(p_filt[p_filt > 0] + eps))
    ent_joint = -np.sum(p_joint[p_joint > 0] * np.log2(p_joint[p_joint > 0] + eps))

    MI = ent_org + ent_filt - ent_joint
    return MI

def naloga4(vhod, prag):
    arr = nalozi_sliko(vhod)
    arr = normaliziraj_sliko(arr)
    arr_filtrirana = filtriraj_fft(arr, prag)
    MI = izracunaj_MI(arr, arr_filtrirana)
    return MI
