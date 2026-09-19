#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

my $source_file = '../file for wed/edward-thorp-tong-hop.html';
my $index_file  = 'index.html';

print "Reading $source_file...\n";
open my $sf, '<:encoding(UTF-8)', $source_file or die "Cannot open $source_file: $!";
my $source_html = do { local $/; <$sf> };
close $sf;

# 1. Extract <style>
my ($style_content) = $source_html =~ m{<style>(.*?)</style>}s;
die "No <style> found" unless defined $style_content;

# Scope CSS
$style_content =~ s{:root\b}{&}g;
$style_content =~ s{\bbody\s*\{}{&.thorp-body \{}g;
$style_content =~ s{\bhtml\s*\{}{&.thorp-html \{}g;

my $scoped_style = <<"CSS";
<style>
#article-thorp-panel {
$style_content
}
</style>
CSS

# 2. Extract <body>
my ($body_content) = $source_html =~ m{<body>(.*?)</body>}s;
die "No <body> found" unless defined $body_content;

my $panel_html = <<"HTML";
<div id="article-thorp-panel" class="sukien-article-panel thorp-body">
$scoped_style
    <div style="padding: 16px 20px; background: #e6ede4;">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: #14402f; border: 1px solid #c6d1c5; padding: 7px 16px; cursor: pointer; background: #f3f6f0; font-family: inherit; font-size: 0.95rem; border-radius: 4px; font-weight: 600;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
$body_content
    <div style="padding: 20px; text-align: center; background: #e6ede4;">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: #14402f; border: 1px solid #c6d1c5; padding: 7px 16px; cursor: pointer; background: #f3f6f0; font-family: inherit; font-size: 0.95rem; border-radius: 4px; font-weight: 600;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
</div>
HTML

# 3. Read index.html
print "Reading $index_file...\n";
open my $inf, '<:encoding(UTF-8)', $index_file or die "Cannot open $index_file: $!";
my $index_html = do { local $/; <$inf> };
close $inf;

# A. Add fonts if not present
my $font_tag = '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet">';
if ($index_html !~ /Bricolage\+Grotesque/) {
    $index_html =~ s{(<link href="https://fonts\.googleapis\.com/css2\?family=Source\+Serif\+4:[^"]+" rel="stylesheet">)}{$1\n    $font_tag};
    print "Added Google fonts\n";
}

# B. Insert card into Trang Chu (Home) news-list
my $home_card = <<"HCARD";
                        <!-- Post: Edward Thorp (Huyen Thoai) -->
                        <a href="/huyen-thoai/edward-thorp" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-crown"></i> Huyền thoại &amp; Tài chính</span>
                                <span class="news-time">19/09/2026</span>
                            </div>
                            <h3 class="news-heading">Edward Thorp — Giáo Sư Đếm Bài, Thắng Cả Sòng Bạc Lẫn Phố Wall</h3>
                            <p class="news-excerpt">Câu chuyện về một cậu bé nghèo thích nghịch hóa chất, người chứng minh rằng toán học kiếm được tiền ở cả bàn blackjack lẫn sàn chứng khoán.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
HCARD

if ($index_html !~ /id="panel-trang-chu".*?href="\/huyen-thoai\/edward-thorp"/s) {
    # Insert at top of news-list in panel-trang-chu
    $index_html =~ s{(<div id="panel-trang-chu" class="tab-panel active">\s*<h2 class="section-title"><i class="fa-solid fa-fire-flame-curved"></i> Bài viết mới</h2>\s*<div class="news-list">)}{$1\n$home_card}s;
    print "Added card to Trang Chu (Home)\n";
} else {
    print "Card already exists in Trang Chu\n";
}

# C. Insert card into Huyen Thoai news-list
my $ht_card = <<"HTCARD";
                        <!-- Post: Edward Thorp -->
                        <a href="/huyen-thoai/edward-thorp" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-crown"></i> Toán học &amp; Định lượng</span>
                                <span class="news-time">14/08/1932 – nay</span>
                            </div>
                            <h3 class="news-heading"><span style="font-size:0.75em;color:#6fae6a;font-weight:500;display:block;margin-bottom:2px;letter-spacing:0.04em;">Toán học &amp; Tài chính định lượng</span>Edward Thorp — Giáo Sư Đếm Bài, Thắng Cả Sòng Bạc Lẫn Phố Wall</h3>
                            <p class="news-excerpt">Từ một cậu bé nghèo nghịch hóa chất đến người chứng minh toán học có thể đánh bại casino và thị trường chứng khoán — cha đẻ của đầu tư định lượng hiện đại.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
HTCARD

if ($index_html !~ /id="panel-huyen-thoai".*?href="\/huyen-thoai\/edward-thorp"/s) {
    # Insert at top of news-list in panel-huyen-thoai (before FDR card)
    my $ht_target = '<!-- Post: FDR Luoc Su (Thu Vien) -->';
    if ($index_html =~ /\Q$ht_target\E/) {
        $index_html =~ s{\Q$ht_target\E}{$ht_card\n$ht_target};
        print "Added card to Huyen Thoai\n";
    } else {
        # Fallback to news-list in panel-huyen-thoai
        $index_html =~ s{(<div id="panel-huyen-thoai"[^>]*>.*?<div class="news-list">)}{$1\n$ht_card}s;
        print "Added card to Huyen Thoai (fallback)\n";
    }
} else {
    print "Card already exists in Huyen Thoai\n";
}

# D. Insert article panel
if ($index_html !~ /id="article-thorp-panel"/) {
    my $panel_target = '</div><!-- /#huyen-thoai-article-view -->';
    if ($index_html =~ /\Q$panel_target\E/) {
        $index_html =~ s{\Q$panel_target\E}{$panel_html\n$panel_target};
        print "Added article-thorp-panel\n";
    } else {
        die "Could not find panel target: $panel_target\n";
    }
} else {
    print "Panel already exists in index.html\n";
}

# Write index.html
open my $outf, '>:encoding(UTF-8)', $index_file or die "Cannot write $index_file: $!";
print $outf $index_html;
close $outf;
print "Successfully updated $index_file!\n";
